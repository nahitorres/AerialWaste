# Standard libraries
import sys
sys.path.append("..")
import os
import json

# Third-party libraries
import cv2
import torch
import imageio
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from matplotlib import pyplot as plt

# Local libraries
from utils import imutils as imutils

def calculate_label_array(categories, cats):
    labels = []
    
    for x in cats:
        labels.append(1 if x in categories else 0)
    
    return np.array(labels)

def load_image_label_list_from_json(dataset_json, binary, classes):

    with open(dataset_json,"r") as filecontent:
        data = json.load(filecontent)
    results = []
    if not binary:
        cats_ids = [cat["id"] for cat in data["categories"]]
        if type(classes) == list:
            for c in classes:
                if not c in cats_ids:
                    raise Exception("Invalid categories", classes)
        else:
            classes = cats_ids
    for img in data["images"]:
        if binary:
            cats = np.array([img["is_candidate_location"]]) 
            results.append(cats)
        else:
            if img["valid_fine_grain"]:
                cats = calculate_label_array(img["categories"], classes)
                results.append(cats)
    return np.array(results)

def get_img_path(img_name, dataset_root):
    return os.path.join(dataset_root, img_name)

def ok(img_cats, cats):
    for c in img_cats:
        if c in cats:
            return True
    return False

def load_img_name_list(dataset_json, binary, classes):
    with open(dataset_json,"r") as filecontent:
        data = json.load(filecontent)
    if binary:
        img_name_list = [img["file_name"] for img in data["images"]]
    else:
        cats_ids = [cat["id"] for cat in data["categories"]]
        if type(classes) == list: 
            for c in classes:
                if not c in cats_ids:
                    raise Exception("Invalid categories", classes)
        else:
            classes = cats_ids
        img_name_list = [img["file_name"] for img in  data["images"] if img["valid_fine_grain"] and ok(img["categories"], classes)]

    return img_name_list


class ImageDataset(Dataset):

    def __init__(self, dataset_json, dataset_root,
                 resize_long=None, rescale=None, 
                 flip=False,
                 crop_size=None, crop_method=None, debug_param=False, to_torch=True, binary=True, classes=None):
       
        self.dataset_json = dataset_json
        self.img_name_list = load_img_name_list(dataset_json, binary, classes)

        self.dataset_root = dataset_root

        self.resize_long = resize_long
        self.rescale = rescale
        self.crop_size = crop_size
        self.flip = flip
        self.crop_method = crop_method
        self.to_torch = to_torch

        self.debug_param = debug_param
        
        self.label_list = load_image_label_list_from_json(self.dataset_json, binary, classes)
        
    def __len__(self):
        return len(self.img_name_list)

    def __getitem__(self, idx):
        name_str = self.img_name_list[idx]
        img_path = get_img_path(name_str, self.dataset_root)

        img = Image.open(img_path)
        if img.mode not in ('L', 'RGB'):
            img = img.convert('RGB')
        img = np.asarray(img)


        if self.debug_param:
            plt.imshow(img)
            plt.show()

        if self.resize_long:
            img = imutils.random_resize_long(img, self.resize_long[0], self.resize_long[1])
            if self.debug_param:
                print("Resize")
                plt.imshow(img)
                plt.show()

        if self.rescale:
            img = imutils.random_scale(img, scale_range=self.rescale, order=3)
            if self.debug_param:
                print("Rescale")
                plt.imshow(img)
                plt.show()

        if self.flip:
            img = imutils.random_flip(img)
            if self.debug_param:
                print("Flip")
                plt.imshow(img)
                plt.show()

        if self.crop_size:
            if self.crop_method == "random":
                img = imutils.random_crop(img, self.crop_size, 0)
                if self.debug_param:
                    print("Crop random")
                    plt.imshow(img)
                    plt.show()
            else:
                img = imutils.top_left_crop(img, self.crop_size, 0)
                if self.debug_param:
                    print("Crop not random")
                    plt.imshow(img)
                    plt.show()

        if self.to_torch:
            img = imutils.hwc_to_chw(img)


        return {'name': name_str, 'img': img}

class ClassificationDataset(ImageDataset):

    def __init__(self, dataset_json, dataset_root,
                 resize_long=None, rescale=None, 
                 flip=False,
                 crop_size=None, crop_method=None, debug_param=False, binary=True, classes=None):
        
        super().__init__(dataset_json, dataset_root,
                 resize_long, rescale,  flip,
                 crop_size, crop_method, debug_param, binary=binary, classes=classes)
        

    def __getitem__(self, idx):
        out = super().__getitem__(idx)
        out['label'] = torch.from_numpy(self.label_list[idx])
        return out

