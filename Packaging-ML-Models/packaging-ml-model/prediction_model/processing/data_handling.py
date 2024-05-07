import os
import pandas as pd 
import joblib

from prediction_model.config import config

print(config.say())

def load_dataset(file_name):
    file_path=os.join(config.DATAPATH,file_name) # Using only join as we are using a path and a string
    _data = pd.read_csv(file_path)
    return _data

# Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME) # Using path as we are joining 2 paths
    joblib.dump(pipeline_to_save,save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

# Deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME) 
    model_loaded=joblib.load(pipeline_to_load,save_path)
    print(f"Model has been loaded under the name {config.MODEL_NAME}")
    return model_loaded  