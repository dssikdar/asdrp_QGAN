# How to make the MolGAN code work in Jupyter Notebook
## A few very simple steps you need to follow.

### Step One
First, run
> `pip install wget`
> `pip install torch`
> `pip install pandas`
> `pip install numpy`

to install all the modules.

### Step Two
Next go find and replace all `torch.cuda.FloatTensor` to `torch.FloatTensor` if you don't have an NVIDIA GPU.
This will solve the Torch CUDA error, but will make training a bit slower.  
Change
```python
cuda = True if torch.cuda.is_available() else False
  if cuda:
    self.G.cuda()
    self.D.cuda()
self.Tensor = torch.cuda.FloatTensor if cuda else torch.FloatTensor
```
to
```python
cuda = False
self.Tensor = torch.FloatTensor
```

### Step 3
To prevent the **FileNotFound** error, change the folder name below to anything you want.
```python
trainer = TrainModelRunner('X_JTVAE_250k_rndm_zinc.csv', output_model_folder='your_folder_name', starting_epoch=200, save_interval=100, message='Starting training', batch_size=2500)
```

#### That's it! You're all ready to run the MolGAN code!
> @PNGNS-Marekos1111
