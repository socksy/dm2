# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%matplotlib inline

# <codecell>

import numpy as np
import pandas as pd
import sklearn
import csv as csv
import matplotlib.pyplot as plt

# <rawcell>

# opening training data set from the directory you are in 

# <codecell>

auto=pd.read_csv("carTrainingData.csv","auto",delimiter=',')
auto.head()

# makes them into a matrix
#with open('carTrainingData.csv','rb') as carTrainingData:
 #   csv_file_object = csv.reader(carTrainingData) 
  #  header = csv_file_object.next()
    
   # training_data=[]
    #for row in csv_file_object:
     #   training_data.append(row)
    #training_data=np.array(training_data)

# <rawcell>

# opening test data set from the directory you are in 

# <codecell>

autotest=pd.read_csv("carTestData.csv","auto",delimiter=',')
autotest.head()

#makes it into a matrix
#with open('carTestData.csv','rb') as carTestData:
 #  csv_file_object = csv.reader(carTestData) 
  #  header = csv_file_object.next()
   # 
    #test_data=[]
    #for row in csv_file_object:
     #   test_data.append(row)
    #test_data=np.array(test_data)

# <codecell>

auto.dtypes

# <codecell>

auto.describe()

# <rawcell>

# there are 56303 observations, shows all variable names and where NA's have appeared 

# <codecell>

auto=auto.fillna(auto.mean())
#auto.describe()
auto.head()

# <rawcell>

# Data set cleaned and missing data filled with the mean
# Vehicle year and Age are similar so consider just age 
# make,model, sub model, only consider make to begin with? if time maybe see if model has an effect as well

# <codecell>

auto.groupby('Make').IsBadBuy.sum().plot(kind='bar')

# <rawcell>

# from the plot above it can be seen that 'make' is a affects how many IsBadBuy's there are

# <codecell>

auto.boxplot(column='VehicleAge',by='Make',grid=False)

# <rawcell>

# shows that there is a range of ages for each model so maybe vehicle age is factor of model when predicting IsBadBuy

# <codecell>

auto.boxplot(column='VehicleAge',by='IsBadBuy',grid=False )

# <codecell>

auto.groupby('Size').IsBadBuy.sum().plot(kind='bar')

# <codecell>

auto.boxplot(column='MMRAcquisitionRetailAveragePrice',by='IsBadBuy',grid=False)

# <codecell>

auto.boxplot(column='MMRAcquisitionAuctionAveragePrice',by='VehicleAge',grid=False)

# <codecell>

auto.boxplot(column='MMRAcquisitionAuctionAveragePrice',by='IsBadBuy',grid=False)

# <codecell>

auto.groupby('WheelType').IsBadBuy.sum().plot(kind='bar')

