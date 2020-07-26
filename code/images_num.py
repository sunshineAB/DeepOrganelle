#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/28 21:13
@Author : Jinghao Peng
@File : images_num.py
@Software: PyCharm
"""
import numpy as np
import os
import shutil

if __name__=='__main__':
  path='d:/home/jhpeng/pjh/ZhangLabData/'

  images='CompleteData'

  cls=['chlo_enlarged','chlo_normal','mito_elongated','mito_normal','pex_elongated','pex_normal']

  for i in cls:
    train_p=path+images+'/train/'+i
    val_p=path+images+'/val/'+i
    test_p=path+images+'/test/'+i

    print('{0:s} train set number: {1:d}'.format(i,len(next(os.walk(train_p))[2])))
    print('{0:s} val set number: {1:d}'.format(i,len(next(os.walk(val_p))[2])))
    print('{0:s} test set number: {1:d}\n'.format(i,len(next(os.walk(test_p))[2])))
