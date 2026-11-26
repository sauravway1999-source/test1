import cv2
import time

image_path = r"C:\Users\Hp\Downloads\mango.png"
# 1. Load the original image
image = cv2.imread(image_path)

# 2. Check image
if image is None:
    print("Image not found!")

else:
    # 3. Resize the image
    image = cv2.resize(image, (800, 400))

    # 4. Draw Circle
    circle_img = image.copy()
    cv2.circle(circle_img, (200, 200), 100, (0, 0, 255), 3)
    cv2.imshow("Circle", circle_img)
    time.sleep(1)

    # 5. Draw Triangle
    triangle_img = image.copy()
    cv2.line(triangle_img, (200, 50), (80, 300), (0, 255, 0), 3)
    cv2.line(triangle_img, (80, 300), (320, 300), (0, 255, 0), 3)
    cv2.line(triangle_img, (320, 300), (200, 50), (0, 255, 0), 3)
    cv2.imshow("Triangle", triangle_img)
    time.sleep(1)

    # 6. Draw Rectangle
    rect_img = image.copy()
    cv2.rectangle(rect_img, (80, 100), (320, 300), (255, 0, 0), 3)
    cv2.imshow("Rectangle", rect_img)
    time.sleep(1)

    # 7. Draw Arrow
    arrow_img = image.copy()
    cv2.arrowedLine(arrow_img, (50, 350), (300, 100), (255, 255, 0), 3)
    cv2.imshow("Arrow", arrow_img)
    time.sleep(1)

    # 8. Wait for key press
    cv2.waitKey(0)

    # 9. Close all windows
    cv2.destroyAllWindows()
