from deepface_functions import face_verify
from deepface_recognition import face_recogn
from deepface_analyze import face_analyze

def main():
    # 1. Приклад використання face_verify
    img_path_1 = 'faces/1.jpg'
    img_path_2 = 'faces/a4.jpg'
    verification_result = face_verify(img_1=img_path_1, img_2=img_path_2)
    print(f"Verification Result: {'Провірка пройдена✔️. Пропустити!!!' if verification_result else 'Затримати!!!🚓🚨'}")

    # 2. Приклад використання face_recogn
    recognition_result = face_recogn(img_path='faces/000001.jpg', db_path='faces')
    print("Recognition Result:", recognition_result)

    # 3. Приклад використання face_analyze
    face_analyze()

if __name__ == '__main__':
    main()
