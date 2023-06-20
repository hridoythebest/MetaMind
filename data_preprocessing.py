def preprocess_data(data):
    # Perform data preprocessing steps
    
    # Preprocess x_train and y_train
    x_train = preprocess_x(data)
    y_train = preprocess_y(data)
    
    # Return the preprocessed data as an object
    return PreprocessedData(x_train, y_train)

def preprocess_x(data):
    # Implement your data preprocessing steps for x_train here
    # ...
    return preprocessed_x

def preprocess_y(data):
    # Implement your data preprocessing steps for y_train here
    # ...
    return preprocessed_y

class PreprocessedData:
    def __init__(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

