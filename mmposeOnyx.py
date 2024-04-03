import torch.onnx
import torch

# Assuming `model` is your PyTorch model and `dummy_input` is a tensor appropriate for your model input
dummy_input = torch.randn(1, 3, 224, 224)  # Example input; adjust the size as per your model's requirement
torch.onnx.export(model, dummy_input, "model.onnx")
