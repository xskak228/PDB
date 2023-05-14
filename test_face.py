import cv2
import dlib

def detect_face(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Создание детектора лиц с использованием предобученной модели
    face_detector = dlib.get_frontal_face_detector()

    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на изображении
    faces = face_detector(gray)

    if len(faces) > 0:
        # Нахождение координат лица
        face = faces[0]
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Вычисление середины лица
        center_x = x + w // 2
        center_y = y + h // 2

        # Определение размеров для обрезки изображения
        target_width = 500
        target_height = 300

        # Вычисление границ обрезки
        left = max(0, center_x - target_width // 2)
        right = min(image.shape[1], center_x + target_width // 2)
        top = max(0, center_y - target_height // 2)
        bottom = min(image.shape[0], center_y + target_height // 2)

        # Обрезка изображения
        cropped_image = image[top:bottom, left:right]

        # Изменение размера обрезанного изображения до 500x300
        cropped_image = cv2.resize(cropped_image, (500, 300))

        # Вывод результата обрезанного изображения
        cv2.imshow("Cropped Image", cropped_image)
        cv2.waitKey(0)
    else:
        print("Лицо не обнаружено на изображении.")

    cv2.destroyAllWindows()

# Пример использования
image_path = "test_img.JPG"
detect_face(image_path)
