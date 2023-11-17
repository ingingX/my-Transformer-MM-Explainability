
# import needed modules
import os
import shutil

# read image ids from txt, save to a list
image_id_list_path = './image_ids.txt'

with open(image_id_list_path, 'r') as file:
    lines = [line.split(', ') for line in file]
    image_id_list = lines[0]

# path to VQA_v2 image dataset, val part
mscoco_val_dataset_path = '/Users/elyjahma/Downloads/mscoco/jpg/val2014'
# path to VQA_v2 image dataset, train part
mscoco_train_dataset_path = '/Users/elyjahma/Downloads/mscoco/jpg/train2014'
# path to VQA_v2 image dataset, test part
mscoco_test_dataset_path = '/Users/elyjahma/Downloads/mscoco/jpg/test2015'

# path to to-use image data set
to_use_dataset_path = '/Users/elyjahma/Downloads/to_use_image'
os.makedirs(to_use_dataset_path, exist_ok=True)

count = 0
to_use_image_id_list = []
# Reading all files in the source folder
for file_name in os.listdir(mscoco_val_dataset_path):
    if file_name[-10:-4] in image_id_list:
        full_to_use_file_path = os.path.join(mscoco_val_dataset_path, file_name)
        # Copy file to the destination folder
        shutil.copy(full_to_use_file_path, to_use_dataset_path)
        to_use_image_id_list.append(file_name[-10:-4])
        count = count + 1

print('total to-use image number: ', count)

with open('to_use_image_ids.txt', 'w') as file:
    file.write(', '.join(to_use_image_id_list))
