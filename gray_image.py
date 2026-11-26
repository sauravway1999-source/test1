import cv2

image_path = r"C:\Users\Hp\Downloads\mango.png"

# 1. READ the image data from the path
image = cv2.imread(image_path)

# 2. CHECK if the image actually loaded
if image is None:
    print("Error: Could not open or find the image. Check if the file path is correct!")
else:
    # 3. CONVERT the color image to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4. DISPLAY the Grayscale image
    cv2.imshow("Original Image", image)
    cv2.waitKey(590)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
