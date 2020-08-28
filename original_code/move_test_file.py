import os
import shutil

from tqdm import tqdm

from class_list import LabelList


# billboard_***_test.txt内の画像をdetect.py用にdata/samplesに保存する
def main(label_name):
    # data/samples内の画像を一度削除する
    os.system('rm data/samples/*.jpg')
    with open('./data/billboard_' + label_name + '_test.txt', 'r', encoding='utf-8') as billboard:
        image_path_list = billboard.readlines()
        for image_path in tqdm(image_path_list):
            image_path = image_path.replace('\n', '')
            shutil.copyfile(image_path, './data/samples/' + os.path.basename(image_path))


# bad, goodファイル内に記述されたファイルをtest_image/に保存する
def confirm_good_bad(label_name, result_file_list):
    os.system('rm test_image/*/*.jpg')
    for i, result_file in enumerate(result_file_list):
        image_path_list = result_file.readlines()
        for image_path in tqdm(image_path_list):
            image_path = os.path.join('./output/', image_path)
            image_path = image_path.replace('\n', '')
            if i == 0:
                save_path = './test_image/' + label_name + '/good/' + os.path.basename(image_path)
            elif i == 1:
                save_path = './test_image/' + label_name + '/bad/' + os.path.basename(image_path)
            shutil.copyfile(image_path, save_path)


if __name__ in '__main__':
    _, label_name = LabelList.ALL.value
    main(label_name)

    # with open('./results/' + label_name + '_good_result.txt', 'r', encoding='utf-8') as good_result_file, \
    #         open('./results/' + label_name + '_bad_result.txt', 'r', encoding='utf-8') as bad_result_file:
    #     confirm_good_bad(label_name, [good_result_file, bad_result_file])
