import torch
from torchvision import  transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import os

# Função para carregar e transformar a imagem
def load_image(image_path):
    img = Image.open(image_path)

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    img_t = preprocess(img)
    batch_t = torch.unsqueeze(img_t, 0)
    return batch_t

# Função para prever o conteúdo da imagem
def predict_image(image_path):
    model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
    model.eval()
    
    batch_t = load_image(image_path)
    
    with torch.no_grad():
        out = model(batch_t)
    
    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    
    with open("imagenet_classes.txt") as f:
        labels = [line.strip() for line in f.readlines()]
    
    top10 = [(labels[idx], percentage[idx].item()) for idx in indices[0][:10]]
    
    return top10
    
# Exemplo de uso
image_folder = 'imagens'
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder)]

for image_path in image_files:
    predictions = predict_image(image_path)
    print(f"Descrição da imagem '{os.path.basename(image_path)}':")
    for label, score in predictions:
        print(f"  - {label}: {score:.2f}%")
    print()  # Linha em branco para separar resultados
