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
car_model = 0
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
            car_model = car_model+1
        
            for i in files3:
                filename, _ = i.split(".")
                content = open(label_path + l + k + j + filename + '.txt').read()
                if (content[0] != "3"):
                    filenames.append(filename)
                    viewpoints.append(content[0])
                    carmodel_list.append(car_model)
                    year,_ = j.split("/")
                    year_list.append(year)
                    car_make,_ = l.split("/")
                    car_makenames.append(car_make)
        
        
d = {'View Point': viewpoints, 'Filename': filenames, 'CarModel': cartype_list, 'Year': year_list, 'CarMake': car_makenames}
df = pd.DataFrame(data=d)

print(df)
print(df.loc[df['CarModel'] == 1])
