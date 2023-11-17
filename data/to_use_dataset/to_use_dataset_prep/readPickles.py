# read MHUG dataset pickles
# save image ids and question ids to .txt files

# import needed modules
import os
import pickle
import shutil

# mhug pickle path
mhug_pickle_path = './infotech2020_fabian/MHUG/mhug/vqa-mhug_answers.pickle'

# read pickle
with open(mhug_pickle_path, 'rb') as file:
    data = pickle.load(file)

# get question ids and sort
question_id_list = list(set(data.index.get_level_values('question_id').tolist()))

# max_length = len(max(question_id_list, key=len))
# question_id_list = [element.zfill(max_length) for element in question_id_list]
question_id_list.sort()



# get image ids and sort
image_id_list = [q[:-3] for q in question_id_list]
# max_length = len(max(image_id_list, key=len))
# image_id_list = [element.zfill(max_length) for element in image_id_list]
image_id_list.sort()

# total number should be both 3990
print('total question number: ', len(question_id_list))
print('total image number: ', len(image_id_list))

# save the ids to .txt files
with open('question_ids.txt', 'w') as file:
    file.write(', '.join(question_id_list))
with open('image_ids.txt', 'w') as file:
    file.write(', '.join(image_id_list))

