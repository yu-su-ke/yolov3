import glob
import os


name_list = ['train', 'val', 'test']

for name in name_list:
    train_path = glob.glob('../../billboard/images/{}/*'.format(name))

    with open('../data/billboard_all_{}.txt'.format(name), 'w', encoding='utf-8') as text_file:
        for path in train_path:
            image_name = os.path.basename(path)
            text_file.write('../billboard/images/{}\n'.format(image_name))