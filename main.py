# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:36:20 2022

@author: asus-pc
"""
#imports
import os
import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt # PyPlot for visualize images
import numpy as np              # numpy library
import cv2                      #Open-CV libraries
import pandas as pd


path = "F:/Image_data/data/image/" # image file path
label_path = "F:/Image_data/data/label/" # label file path

files = os.listdir(path)



viewpoints = []
filenames = []
carmodel_list = []
year_list = []
car_makenames = []

for l in files:
    l = l + "/"
    files1 = os.listdir(path + l) 
    for k in files1:
        k = k + "/"
        files2 = os.listdir(path + l + k) 
    
        for j in files2:
            j = j + "/"
            files3  = os.listdir(path + l + k + j) 
    
            for i in files3:
                filename, _ = i.split(".")
                content = open(label_path + l + k + j + filename + '.txt').read()
                if (content[0] != "3") & (content[0] != "-"):
                    filenames.append(filename)
                    viewpoints.append(content[0])
                    year,_ = j.split("/")
                    year_list.append(year)
                    car_make,_ = l.split("/")
                    car_makenames.append(car_make)
                    car_model,_ = k.split("/")
                    carmodel_list.append(car_model)
        
        
d = {'View Point': viewpoints, 'Filename': filenames, 'CarModel': carmodel_list, 'Year': year_list, 'CarMake': car_makenames}
df = pd.DataFrame(data=d)


df_front = df[df['View Point'] == "1"]
df_front_side = df[df['View Point'] == "4"]
df_front_all = pd.concat([df_front, df_front_side])
df_rear = df[df['View Point'] == "2"]
df_rear_side = df[df['View Point'] == "5"]
df_rear_all = pd.concat([df_rear, df_rear_side])
print(df_front_all)
print(df_rear_all)
print(df)

