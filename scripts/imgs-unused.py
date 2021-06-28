import os
import sys
from queue import Queue
from typing import List

# Define the extensions of target files
img_exts = ['.png', '.jpg', '.bmp', '.gif']
doc_exts = ['.md', '.markdown']


# Get filesets by extensions as a collection
def _find_files(path: str, exts: List[str]) -> List[str]:
    queue = Queue()
    matched_files = list()

    queue.put(path)
    while not queue.empty():
        file_path = queue.get()
        if os.path.isdir(file_path):
            for sub_file in os.listdir(file_path):
                queue.put(file_path + '/' + sub_file)
        elif os.path.isfile(file_path) and os.path.splitext(file_path)[1] in exts:
            matched_files.append(file_path)

    return matched_files


# Get unused image collection
def find_unused_imgs(root_path: str) -> List[str]:
    doc_paths = _find_files(root_path, doc_exts)
    img_paths = _find_files(root_path, img_exts)

    for doc_path in doc_paths:
        with open(doc_path, 'r', encoding='UTF-8') as fp:
            doc_data = fp.read()
            used_imgs_path = []
            for img_path in img_paths:
                if os.path.split(img_path)[1] in doc_data:
                    used_imgs_path.append(img_path)
            img_paths = list(set(img_paths).difference(set(used_imgs_path)))

    return img_paths


if __name__ == '__main__':
    docs_path = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] is not None else os.path.abspath('./'))

    unused_imgs = find_unused_imgs(docs_path)

    if len(unused_imgs) == 0:
        print("There is no unused image in '{}'.".format(docs_path))
    else:
        print("There are {} unused images in '{}':".format(len(unused_imgs), docs_path))
        for i in range(len(unused_imgs)):
            print("[{}] {}".format(i + 1, unused_imgs[i]))
