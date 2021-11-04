# asdrp_QGAN

![image](https://user-images.githubusercontent.com/69136009/136667976-293df844-9489-45c4-ad11-dee2fde80661.png)

Welcome to the ASDRP Quantum Generative Adversarial Network (QGAN) repository. 

Abstract: Current drug discovery pipelines take between five to ten years and cost billions of dollars. People have been researching and implementing computational approaches to search for molecules and compounds from the chemical space, which can be on the order of 1060. One solution is deep generative models, which can learn from the nonlinearity in data by modeling the probability distribution of chemical structures and drugs. These generative models can extract salient features which characterize the molecules. One of the most well-known unsupervised learning algorithms –– Generative Adversarial Networks (GANs) –– can discover drug candidates as they generate molecular structures abiding by the laws of physics and chemistry. However, GANs often suffer from problems, including vanishing gradient and increasing complexity, due to the exponential increase in volume of data. 
We need a generative model that can better learn the representation of molecules more efficiently than classical ML models by searching the exponentially large chemical space. Quantum computing is better than classical computing at processing high dimensional data because qubits can represent exponentially more states than bits at the same time. While n number of bits can represent 2n possible states, n qubits can represent 2n states. For example, 64 bits can represent 128 states, while 64 qubits can represent 264 (~18 billion) states. Because of the immense power of qubits, which is necessary for searching the chemical space, we propose a QGAN with a hybrid architecture: a quantum generator and a classical discriminator. The quantum generator would use a series of variational quantum circuits to automatically learn features and efficiently train the QML model. The discriminator will likely be a classical neural network, which would classify between the fake and real molecular structures. 

Keywords:
Quantum Machine Learning, Generative Adversarial Learning, Variational Quantum Circuits (VQC), Discriminator, Generator

Created by: Diptanshu Sikdar

Current Advisor: Dr. Larry McMahan

Current researchers: Diptanshu Sikdar, Max Cui, Adelina Chau, Arjun Bhamra, Joey Huang, Kanthi Makineedi, 

Navigation Guide:
1. Main 
2. Chemistry <branch>
