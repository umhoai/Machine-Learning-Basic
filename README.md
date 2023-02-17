# define your PyTorch model
model = MyPyTorchModel()

# load the TensorFlow checkpoint
checkpoint = torch.load("my_checkpoint.pth", map_location=torch.device('cpu'))

# set from_tf=True to load a TensorFlow checkpoint into a PyTorch model
model.load_state_dict(checkpoint['model_state_dict'], from_tf=True)
