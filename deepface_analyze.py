from deepface import DeepFace
import json
import pandas as pd

def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path='faces/000007.jpg', actions=['age', 'gender', 'race', 'emotion'])

        if isinstance(result_dict, list):
            result_dict = result_dict[0]

        verified = result_dict.get("verified", False) if isinstance(result_dict, dict) else False
        result_dict["verified"] = bool(verified)

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print(f'[+] Race:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

    except Exception as _ex:
        return str(_ex)
