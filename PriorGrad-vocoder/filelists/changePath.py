import os

source_path = "/path/to/your/"
replacement_path = "/home/ytang363/NeuralSpeech/PriorGrad-vocoder/"

input_txt = '/home/ytang363/NeuralSpeech/PriorGrad-vocoder/filelists/test.txt'
output_txt = '/home/ytang363/NeuralSpeech/PriorGrad-vocoder/filelists/newPath_test.txt'

with open(input_txt, "r") as file:
    content = file.read()
    modified_content = content.replace(source_path, replacement_path)
print(modified_content)

with open(output_txt, "w") as file:
    file.write(modified_content)