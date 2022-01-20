# ASDRP Quantum Generative Adversarial Network

![image](https://user-images.githubusercontent.com/69136009/136667976-293df844-9489-45c4-ad11-dee2fde80661.png)

Welcome to the ASDRP Quantum Generative Adversarial Network (QGAN) repository. 

Abstract: 
    Current drug discovery pipelines take between five to ten years and cost billions of dollars. As a result, scientists are researching computational approaches to search for molecules from the chemical space. One solution is deep generative models, which learn from the nonlinear data by modeling the probability distribution of chemical structures. These generative models can extract salient features which characterize the molecules. One of the most well-known unsupervised learning algorithms––Generative Adversarial Networks (GANs)––can discover valid drug candidates that abide by the laws of physics and chemistry. However, GANs often suffer from problems, including vanishing gradient and increasing complexity, due to the exponential increase in the volume of data. 
    We need a generative model that can better learn the representation of molecules more efficiently than classical ML models by searching the exponentially large chemical space. Quantum computing is better than classical computing at processing high dimensional data because qubits can represent exponentially more states than bits at the same time. Because of the immense power of qubits and parallelization possible, which is necessary for searching the chemical space, we propose a Quantum Generative Adversarial Network with a hybrid architecture: a quantum generator and a classical discriminator. The quantum generator, a variational quantum circuit, would automatically learn features and generate valid molecules. The discriminator is a classical neural network, which classifies the fake and real molecular structures. The QGAN would learn from more than 100,000 molecules represented by adjacency lists.


Keywords:
Quantum Machine Learning, Generative Adversarial Learning, Variational Quantum Circuits (VQC), Discriminator, Generator

Created by: Diptanshu Sikdar

Current Advisor: Dr. Larry McMahan

Current researchers: Diptanshu Sikdar, Max Cui, Adelina Chau, Arjun Bhamra, Kanthi Makineedi, Sathvik Prasanna

Previous researchers: Joey Huang

Navigation Guide:
1. Main 
2. Chemistry <branch>
