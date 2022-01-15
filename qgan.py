# All Imports
import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math
import random

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()

#from __future__ import print_function, division

from keras.datasets import mnist
from keras.layers.merge import _Merge
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from tensorflow.keras.optimizers import RMSprop
from functools import partial

import keras.backend as K
import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.metrics import mean_squared_error

import QuantumGenerator

class RandomWeightedAverage(_Merge):
    def _merge_function(self, inputs): 
        alpha = K.random_uniform((8, 1, 1, 1))
        return (alpha * inputs[0]) + ((1 - alpha) * inputs[1])

class QGAN():
    def __init__(self):
        self.mol_vec_size = 69
        self.mol_shape = (self.mol_vec_size)
        self.latent_dim = 4
        
        self.n_critic = 5
        optimizer = RMSprop(lr=0.00005)
        
        self.generator = self.build_generator()
        self.critic = self.build_critic()
        
        # Freeze generator's layers while training critic
        self.generator.trainable = False
        
        # Molecule Vector input (real sample)
        real_mol = Input(shape=self.mol_shape)
        
        # Noise input
        z_disc = Input(shape=(self.latent_dim,))
        # Generator molecule (fake sample)
        fake_mol = self.generator(z_disc)
        
        # Discriminator determines validity of the real and fake molecules
        fake = self.critic(fake_mol)
        valid = self.critic(real_mol)
        
        # Construct weighted average
        interpolated_mol = RandomWeightedAverage()([real_mol, fake_mol])
        # Determine validity of weighted sample
        validity_interpolated = self.critic(interpolated_mol)
        
        # Use Python partial to provide loss function 
        partial_gp_loss = partial(self.gradient_penalty_loss, averaged_samples=interpolated_mol)
        partial_gp_loss.__name__ = 'gradient_penalty' 

        self.critic_model = Model(inputs=[real_mol, z_disc], outputs=[valid, fake, validity_interpolated])
        self.critic_model.compile(loss=[self.loss, self.loss, partial_gp_loss], optimizer=optimizer)
        
        # Construct Computational Graph
        self.critic.trainable = False
        self.generator.trainable = True

        # Sampled noise for input to generator
        z_gen = Input(shape=(self.latent_dim,))
        # Generate images based of noise
        mol = self.generator(z_gen)
        # Discriminator determines validity
        valid = self.critic(mol)
        # Defines generator model
        self.generator_model = Model(z_gen, valid)
        self.generator_model.compile(loss=self.loss, optimizer=optimizer)
        
    def gradient_penalty_loss(self, y_true, y_pred, averaged_samples):
        """
        Computes gradient penalty based on prediction and weighted real / fake samples
        """
        gradients = K.gradients(y_pred, averaged_samples)[0]
        gradients_sqr = K.square(gradients)
        gradients_sqr_sum = K.sum(gradients_sqr,
                                  axis=np.arange(1, len(gradients_sqr.shape)))
        gradient_l2_norm = K.sqrt(gradients_sqr_sum)
        gradient_penalty = K.square(1 - gradient_l2_norm)
        return K.mean(gradient_penalty)
    
    def loss(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred)
    
    def build_generator(self):
        QuantumGenerator.buildCircuit()
        
    def build_critic(self):
        model = Sequential()

        model.add(Conv2D(16, kernel_size=3, strides=2, input_shape=self.mol_shape, padding="same"))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Conv2D(32, kernel_size=3, strides=2, padding="same"))
        model.add(ZeroPadding2D(padding=((0,1),(0,1))))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Conv2D(64, kernel_size=3, strides=2, padding="same"))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Conv2D(128, kernel_size=3, strides=1, padding="same"))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(1))

        model.summary()

        molecule = Input(shape=self.mol_shape)
        validity = model(molecule)

        return Model(molecule, validity)        
        
    def gradient_penalty_loss(self, y_true, y_pred, averaged_samples):
        """
        Computes gradient penalty based on prediction and weighted real / fake samples
        """
        gradients = K.gradients(y_pred, averaged_samples)[0]
        gradients_sqr = K.square(gradients)
        gradients_sqr_sum = K.sum(gradients_sqr,
                                  axis=np.arange(1, len(gradients_sqr.shape)))
        gradient_l2_norm = K.sqrt(gradients_sqr_sum)
        gradient_penalty = K.square(1 - gradient_l2_norm)
        return K.mean(gradient_penalty)
        
    #def sample_molecules(self, epoch):
    
    def train(self, epochs, batch_size, dataset, sample_interval=50):
        # Load the dataset
        (X_train, _), (_, _) = dataset
        
        # Adversarial Ground Truths
        valid = -np.ones((batch_size, 1))
        fake = np.ones((batch_size, 1))
        dummy = np.zeros((batch_size, 1)) 
        for epoch in range(epochs):
            for _ in range(self.n_disc):
                #---------------------------#
                #  Train the Discriminator  #
                #---------------------------#
                
                # Select a random batch of molecules 
                idx = np.random.randint(0, X_train.shape[0], batch_size)
                molecule = X_train[idx]
                # Sample Generator Input
                noise = np.random.normal(0, 1, (batch_size, self.latent_dim))
                # Train the critic
                d_loss = self.critic_model.train_on_batch([molecule, noise], [valid, fake, dummy])
            
            
            #-----------------------#
            #  Train the Generator  #
            #-----------------------#
            g_loss = self.generator_model.train_on_batch(noise, valid)
            
            # Plot the progress
            print("%d [D loss: %f] [G loss: %f]" % (epoch, d_loss[0], g_loss))
        
if __name__ == '__main__':
    qgan = QGAN()
    qgan.train(epochs=50, batch_size=8, sample_interval=100)