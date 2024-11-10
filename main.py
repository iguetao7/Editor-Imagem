from rembg import remove
from PIL import Image


#Dados de entrada e saída da imagem
input_path = "PythonImg.jpg"
output_path = "pythonSF.png"

#Editando a imagem
inp = Image.open(input_path)
output = remove(inp)

#Salvando a imagem
output.save(output_path)
