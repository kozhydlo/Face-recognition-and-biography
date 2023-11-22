# Збережіть цей код у файлі README.md
# DeepFace Інструменти

Цей набір скриптів на мові Python використовує бібліотеку DeepFace для виконання різних завдань аналізу обличчя. Скрипти, які включені:

- `deepface_analyze.py`: Аналізує обличчя, визначаючи такі атрибути, як вік, стать, раса та емоції зі вхідного зображення.
- `deepface_functions.py`: Надає функцію для перевірки, чи належать два обличчя одній і тій же особі.
- `deepface_recognition.py`: Виконує розпізнавання обличчя для ідентифікації осіб на вхідному зображенні за допомогою передбаченої бази даних.
- `main.py`: Приклад сценарію, що демонструє використання вищезазначених функцій.

## Передумови

Перед запуском скриптів переконайтеся, що у вас встановлені необхідні залежності. Ви можете встановити їх за допомогою наступної команди:

```bash
pip install deepface pandas
```

# Використання

## 1. Перевірка обличчя (deepface_functions.py)
Перевірте, чи два обличчя належать одній і тій же особі.
``` python
from deepface_functions import face_verify

img_path_1 = 'faces/1.jpg'
img_path_2 = 'faces/a4.jpg'
verification_result = face_verify(img_1=img_path_1, img_2=img_path_2)

print("Результат перевірки:", "Пройдено" if verification_result else "Не пройдено")
```

## 2. Розпізнавання обличчя (deepface_recognition.py)
Визначте особи на вхідному зображенні з використанням передбаченої бази даних.
``` python
from deepface_recognition import face_recogn

img_path = 'faces/000001.jpg'
recognition_result = face_recogn(img_path=img_path, db_path='faces')

print("Результат розпізнавання:", recognition_result)
```

## 3. Аналіз обличчя (deepface_analyze.py)
Аналізуйте атрибути обличчя, такі як вік, стать, раса та емоції з вхідного зображення.
``` python
from deepface_analyze import face_analyze

face_analyze()
```

## 4. Приклад Використання (main.py)
Приклад сценарію, який демонструє використання вищезазначених функцій.

``` python
from deepface_functions import face_verify
from deepface_recognition import face_recogn
from deepface_analyze import face_analyze

def main():
    # Приклад перевірки обличчя
    img_path_1 = 'faces/1.jpg'
    img_path_2 = 'faces/a4.jpg'
    verification_result = face_verify(img_1=img_path_1, img_2=img_path_2)
    print("Результат перевірки:", "Пройдено" if verification_result else "Не пройдено")

    # Приклад розпізнавання обличчя
    recognition_result = face_recogn(img_path='faces/000001.jpg', db_path='faces')
    print("Результат розпізнавання:", recognition_result)

    # Приклад аналізу обличчя
    face_analyze()

if __name__ == '__main__':
    main()

```
# Увага
Також, зверніть увагу, що для цієї програми потрібно імпортувати бібліотеку DeepFace. Коли ви вперше запустите файли, відбудеться завантаження трьох модулів DeepFace, обсяг яких становить приблизно 530 МБ.
