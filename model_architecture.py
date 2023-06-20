import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def create_model(input_size, output_size):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(input_size,)))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(output_size, activation='softmax'))
    
    return model
