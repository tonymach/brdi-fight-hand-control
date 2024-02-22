from transformers import VideoMAEImageProcessor, VideoMAEForVideoClassification
import numpy as np
import torch

video = list(np.random.randn(16, 3, 224, 224))

processor = VideoMAEImageProcessor.from_pretrained("MCG-NJU/videomae-small-finetuned-kinetics")
model = VideoMAEForVideoClassification.from_pretrained("MCG-NJU/videomae-small-finetuned-kinetics")

inputs = processor(video, return_tensors="pt")

with torch.no_grad():
  outputs = model(**inputs)
  logits = outputs.logits

predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
