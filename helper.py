import argparse
import os
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--mode', type=int, default=0,
                        help='0 if opencv mode else dlib ')
    parser.add_argument('--path_to_load', type=str, required=True, help='path to load original image from')
    parser.add_argument('--path_to_save',type=str,required=True,help='path to save rotated image to')
    parser.add_argument('--show',type=bool,default=False, help='show result or not')
    parser.add_argument('--rotation_mode',type=int,default=0,help='0 if Pillow rotation , 1 if opencv')
    args = parser.parse_args()
    return args