
# import needed modules
import os
import shutil
import json

# read question ids from txt, save to a list
question_id_list_path = './to_use_dataset/to_use_dataset_prep/question_ids.txt'

with open(question_id_list_path, 'r') as file:
    lines = [line.split(', ') for line in file]
    question_id_list = lines[0]

# print(type(question_id_list[0]))
# path to VQA_v2 question dataset, val part
mscoco_val_dataset_path = '/Users/elyjahma/Downloads/mscoco/json/v2_OpenEnded_mscoco_val2014_questions.json'
# path to VQA_v2 question dataset, train part
mscoco_train_dataset_path = '/Users/elyjahma/Downloads/mscoco/json/v2_OpenEnded_mscoco_train2014_questions.json'
# path to VQA_v2 question dataset, test part
mscoco_test_dataset_path = '/Users/elyjahma/Downloads/mscoco/json/v2_OpenEnded_mscoco_test2015_questions.json'

# path to to-use image data set
to_use_question_path = '/Users/elyjahma/Downloads/to_use_question/to_use_question.json'
# os.makedirs(to_use_question_path, exist_ok=True)

with open(mscoco_val_dataset_path, 'r') as file:
    data = json.load(file)
mscoco_questions = data.get('questions')

mscoco_question_id = []
used = []
count = 0
for coco_q in mscoco_questions:
    coco_q_id = str(coco_q.get('question_id'))
    # print(coco_q_id)
    if coco_q_id in question_id_list:
        # used.append(q)
        # print(q.get('question_id'))
        used.append(coco_q)
        count = count + 1
# print(count)
# print(used)


with open(to_use_question_path, 'w') as file:
    json.dump(used, file)

