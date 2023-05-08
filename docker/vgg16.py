import torch
import torchvision.models as models

# Load the pre-trained VGG16 model
vgg16 = models.vgg16(pretrained=True)

# Save the model to a file
torch.save(vgg16.state_dict(), 'vgg16.pth')