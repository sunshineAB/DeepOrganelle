#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/28 21:13
@Author : Jinghao Peng
@File : dataArgument.py
@Software: PyCharm
"""

import tensorflow as tf
import numpy as np
import cv2
import os
import argparse
import sys

FLAGS = None

def signalArgument(img1, saveImagePath, i, j, cls, category):
    if(category=="train"):
        img2 = cv2.flip(img1, 0)
        # img2=cv2.flip(img,1)
        img3 = np.rot90(img1, k=1)
        img4 = cv2.flip(img3, 0)
        img5 = np.rot90(img1, k=2)
        img6 = cv2.flip(img5, 0)
        img7 = np.rot90(img1, k=3)
        img8 = cv2.flip(img7, 0)

        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_1.jpeg"), img1)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_2.jpeg"), img2)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_3.jpeg"), img3)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_4.jpeg"), img4)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_5.jpeg"), img5)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_6.jpeg"), img6)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_7.jpeg"), img7)
        cv2.imwrite(os.path.join(saveImagePath, cls + "_train_" + str(i) + "_" + str(j) + "_8.jpeg"), img8)

    elif(category=="val"):
        cv2.imwrite(os.path.join(saveImagePath, cls + "_val_" + str(i) + "_" + str(j) + ".jpeg"), img1)

    elif (category == "test"):
        cv2.imwrite(os.path.join(saveImagePath, cls + "_test_" + str(i) + "_" + str(j) + ".jpeg"), img1)


def imageArgument(singleImagePath, saveImagePath, i, cls, category):
    img = cv2.imread(singleImagePath)
    h = img.shape[0]
    w = img.shape[1]

    img1 = img[0:int(h / 2), 0:int(w / 2)]
    img2 = img[int(h / 2):int(h), 0:int(w / 2)]
    img3 = img[0:int(h / 2), int(w / 2):int(w)]
    img4 = img[int(h / 2):int(h), int(w / 2):int(w)]

    '''
    img1=cv2.resize(img1,(512,512))
    img2=cv2.resize(img2,(512,512))
    img3=cv2.resize(img3,(512,512))
    img4=cv2.resize(img4,(512,512))
    '''

    signalArgument(img1, saveImagePath, i, 1, cls, category)
    signalArgument(img2, saveImagePath, i, 2, cls, category)
    signalArgument(img3, saveImagePath, i, 3, cls, category)
    signalArgument(img4, saveImagePath, i, 4, cls, category)

def main(_):
    classes = ["chlo_enlarged", "chlo_normal", "mito_elongated", "mito_normal", "pex_elongated", "pex_normal"]
    category = FLAGS.category
    for cls in classes:
        # The location of the source file, in the format for example "source_path/train/chlo_enlarged/images.jpeg"
        srcPath = os.path.join(FLAGS.source_dir, category, cls)
        # Image save location after data expansion, in the format for example "save_path/train/chlo_enlarged/images.jpeg"
        savePath = os.path.join(FLAGS.save_dir, category, cls)

        if not os.path.exists(savePath):
            os.makedirs(savePath)

        for root, dirs, files in os.walk(srcPath):
            i = 1
            for imageName in files:
                imagePath = os.path.join(root, imageName)
                # print(imagePath)
                imageArgument(imagePath, savePath, i, cls, category)
                i = i + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_dir",
        type=str,
        default="G:/DeepOrganelleDataset/",
        help="The absolute path of your source images directory."
    )
    parser.add_argument(
        "--save_dir",
        type=str,
        default="G:/DeepOrganelleDataset2/",
        help="The absolute path to save the images."
    )
    parser.add_argument(
        "--category",
        type=str,
        default="train",
        help="Data set for data argument."
    )
    FLAGS, unparsed = parser.parse_known_args()

    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
