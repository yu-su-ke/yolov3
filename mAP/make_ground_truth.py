import glob
import json
import os

from tqdm import tqdm

from scripts.extra.intersect_gt_and_dr import adjust_ground_and_detect
from class_list import LabelList


# class MakeGroundTruth:
#     """
#     annotatino_data/ 内のファイルからground-truthを作る
#     """
#     def __init__(self, label_list, label_name):
#         self.base_path = '../../annotation_data/{}_annotation/'.format(label_name)
#         self.label_dictionary = {}
#
#         self.label_list = label_list
#         self.label_name = label_name
#
#     def main(self):
#         directory_path_list = glob.glob(os.path.join(self.base_path, '*'))
#         for directory_path in tqdm(directory_path_list):
#             file_path_list = glob.glob(os.path.join(directory_path, '*.json'))
#             for file_path in file_path_list:
#                 json_file = open(file_path)
#                 asset = json.load(json_file)
#                 self.write_annotation_path_label(asset)
#
#     def write_annotation_path_label(self, asset):
#         file_name = os.path.splitext(asset['asset']['name'])[0]
#         with open('./input/billboard_{}/ground-truth/{}.txt'.format(self.label_name, file_name), 'w',
#                   encoding='utf-8') as text_file:
#             for region in asset['regions']:
#                 label = region['tags'][0]
#                 if label == 'main':
#                     label = region['tags'][1]
#                 x1 = int(region['points'][0]['x'])
#                 y1 = int(region['points'][0]['y'])
#                 x2 = int(region['points'][2]['x'])
#                 y2 = int(region['points'][2]['y'])
#                 text_file.write('{} {} {} {} {}\n'.format(label, x1, y1, x2, y2))


class MakeGroundTruth:
    """
    model_data/ 内のファイルからground-truthを作る
    """
    def __init__(self, label_list, label_name):
        self.base_path = '../../media/model_data/billboard_{}.txt'.format(label_name)
        self.label_dictionary = {}

        self.label_list = label_list
        self.label_name = label_name

    def main(self):
        with open(self.base_path, 'r', encoding='utf-8') as text_file:
            text_lines = text_file.readlines()
        for text_line in text_lines:
            text_line = text_line.replace('\n', '')
            element_list = text_line.split(' ')
            image_path = element_list[0]
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            with open('./input/billboard_{}/ground-truth/{}.txt'.format(self.label_name, image_name), 'w',
                      encoding='utf-8') as ground_truth_file:
                point_label_list = element_list[1:-1]
                for point_label in point_label_list:
                    point_label_split = point_label.split(',')
                    point = point_label_split[:4]
                    label = int(point_label_split[4])
                    ground_truth_file.write('{} {}\n'.format(self.label_list[label], ' '.join(point)))


if __name__ in '__main__':
    label_list, label_name = LabelList.ALL.value

    os.system('rm -rf ./input/billboard_' + label_name + '/ground-truth/*')

    make_ground_truth = MakeGroundTruth(label_list, label_name)
    make_ground_truth.main()

    # ground_truthとdetect両方に存在しないファイルを削除する. これを回すとground-truthがnullになるので最初だけ回す
    adjust_ground_and_detect(label_name)
