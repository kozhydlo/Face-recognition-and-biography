from deepface import DeepFace
import json
import pandas as pd

def face_recogn(img_path, db_path='faces'):
    try:
        result = DeepFace.find(img_path=img_path, db_path=db_path)
        if isinstance(result, pd.DataFrame):
            return result.values
        else:
            return result
    except Exception as _ex:
        return str(_ex)
