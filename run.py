from helper import *
from face_alignment import face_alignment

if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    args = parse_args()
    face_alignment(args)
