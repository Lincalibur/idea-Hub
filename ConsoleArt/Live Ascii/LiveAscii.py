import cv2
import numpy as np
from PIL import Image

# ASCII characters used to create the image
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    range_width = 256 // len(ASCII_CHARS)
    
    for pixel in pixels:
        # Clamp index to avoid out of range errors
        index = min(len(ASCII_CHARS) - 1, pixel // range_width)
        ascii_str += ASCII_CHARS[index]
    
    return ascii_str

def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index + img_width)] for index in range(0, ascii_str_len, img_width)])
    return ascii_img

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to an image object (PIL)
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Convert the image to ASCII
        ascii_image = image_to_ascii(image)
        
        # Clear the screen
        print("\033[H\033[J", end="")
        
        # Print the ASCII image
        print(ascii_image)

        # To exit, press 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
