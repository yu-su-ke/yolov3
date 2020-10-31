import glob
import os


task = 'media'
name_list = ['train', 'val', 'test']

for name in name_list:
    train_path = glob.glob('../../{}/images/{}/*'.format(task, name))

    with open('../data/billboard_all_{}.txt'.format(name), 'w', encoding='utf-8') as text_file:
        for path in train_path:
            image_name = os.path.basename(path)
            text_file.write('../{}/images/{}/{}\n'.format(task, name, image_name))
