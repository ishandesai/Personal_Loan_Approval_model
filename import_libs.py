"""libraries we need for this project
tensorflow.keras.models: to build and train model
pandas: load dataset and manipulation
seaborn,matplotlib,plotly: data visualization
numpy:array manipulation
sklearn: to split testing and training data,to find accuracy of model and plot confusion matrix



"""
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from sklearn import metrics
from  sklearn.preprocessing import StandardScaler, MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Accuracy
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
jtplot.style(theme = 'monokai', context = 'notebook', ticks = True, grid = False)
