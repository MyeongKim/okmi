import os
import glob
from collections import defaultdict

from colored import fg, bg, attr

TEMP_DIR_NAME = 'sample/materialization'
EXCLUDE_FILE_NAME = 'meta.md'


def display_relations_tree():
    target_dir = os.path.dirname(os.path.abspath(__file__)) + "/" + TEMP_DIR_NAME
    glob_file_list = glob.glob(target_dir + '/**', recursive=True)
    file_and_dir_list = [i.split(target_dir + "/")[1] for i in glob_file_list
                         if i.split(target_dir + "/")[1] and EXCLUDE_FILE_NAME not in i]

    display_directory_tree(file_and_dir_list)


def display_directory_tree(file_and_dir_list):
    tree_dict = defaultdict()
    str_print_list = []
    seperator_ori = ''
    seperator = '    '

    for item in sorted(file_and_dir_list, key=lambda i: len(i)):
        _build_tree_dict(item, tree_dict)

    _build_tree_list(tree_dict, str_print_list, seperator, seperator_ori)
    _color_prinit_tree_list(str_print_list, seperator)


def _build_tree_dict(item, tree_dict):
    if len(item.split("/")) == 1:
        tree_dict[item.split("/")[0]] = {}
    else:
        tmp = ''
        for idx, i in enumerate(item.split("/")):
            if idx != len(item.split("/")) - 1:
                if not tmp:
                    tmp = tree_dict[i]
                else:
                    tmp = tmp[i]
                tmp.update({item.split("/")[idx+1]: {}})


def _build_tree_list(tree_dict, str_print_list, seperator, curr_seperator):
    for key in tree_dict:
        if curr_seperator:
            str_print_list.append(curr_seperator + key)
        else:
            str_print_list.append(key)
        if tree_dict[key] != {}:
            _build_tree_list(tree_dict[key], str_print_list, seperator, curr_seperator + seperator)


def _color_prinit_tree_list(str_print_list, seperator):
    depth_1_set = {
        'fg': 'black',
        'bg': 'white',
        'attr': 'bold'
    }
    depth_2_set = {
        'fg': 'orchid',
        'attr': 'bold'
    }
    depth_3_set = {
        'fg': 'light_blue',
        'attr': 'reset'
    }
    depth_4_set = {
        'fg': 'white',
        'attr': 'reset'
    }

    for str in str_print_list:
        if len(str) - len(str.strip()) == 0:
            color = fg(depth_1_set['fg'])
            reset = ''
            if depth_1_set.get('bg'):
                color += bg(depth_1_set['bg'])
            if depth_1_set.get('attr'):
                reset = attr(depth_1_set['attr'])
            print(reset + color + str + attr('reset'))
        elif len(str) - len(str.strip()) is len(seperator)*1:
            color = fg(depth_2_set['fg'])
            reset = ''
            if depth_2_set.get('bg'):
                color += bg(depth_2_set['bg'])
            if depth_2_set.get('attr'):
                reset = attr(depth_2_set['attr'])
            print(reset + color + str + attr('reset'))
        elif len(str) - len(str.strip()) is len(seperator)*2:
            color = fg(depth_3_set['fg'])
            reset = ''
            if depth_3_set.get('bg'):
                color += bg(depth_3_set['bg'])
            if depth_3_set.get('attr'):
                reset = attr(depth_3_set['attr'])
            print(reset + color + str + attr('reset'))
        else:
            color = fg(depth_4_set['fg'])
            reset = ''
            if depth_4_set.get('bg'):
                color += bg(depth_4_set['bg'])
            if depth_4_set.get('attr'):
                reset = attr(depth_4_set['attr'])
            print(color + str + reset + attr('reset'))


def filter_by_ideal():
    pass


def add_relations():
    pass


if __name__ == '__main__':
    display_relations_tree()
