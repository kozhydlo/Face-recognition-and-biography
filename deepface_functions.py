from deepface import DeepFace
import json
import pandas as pd

def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)
        result_dict["verified"] = bool(result_dict.get("verified", False))

        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        return result_dict["verified"]

    except Exception as _ex:
        return str(_ex)
