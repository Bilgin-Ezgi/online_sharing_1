import os
import argparse
import shutil

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', help='Path to images to rename', default='./uploads/user_post')
    return parser.parse_args()

if __name__ == '__main__':

    args = get_parser()

    print(f'Old Directory is {args.folder}')

    new_folder = args.folder + '_renamed'

    print(f'New Directory is {new_folder}')

    os.makedirs(new_folder, exist_ok=True)

    filelist = os.listdir(args.folder)

    print(filelist)

    for filename in filelist:
        name, ext = filename.rsplit('_', 1)
        new_filename = f'{name}.{ext}'
        print(f'Old file: {os.path.join(args.folder, filename)}, New File: {os.path.join(new_folder, new_filename)}')
        shutil.copy(os.path.join(args.folder, filename), os.path.join(new_folder, new_filename))
        