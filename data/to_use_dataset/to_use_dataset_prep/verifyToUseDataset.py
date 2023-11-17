import os
import json

# Specify the folder path
to_use_image_path = './to_use_dataset/to_use_image'
to_use_question_path = './to_use_dataset/to_use_question/to_use_question_1.json'
# List all files and directories in the folder
images = os.listdir(to_use_image_path)
image_id = []
for i in images:
    image_id.append(i[-10:-4])

image_id = [i.lstrip('0') for i in image_id]

with open(to_use_question_path, 'r') as file:
    question = json.load(file)

count = 0
for q in question:
    if str(q.get('image_id')) not in image_id:
        count = count + 1

print('errors: ', count)

