from PIL import Image

def image_to_ascii(image_path, output_file, width=100):
    # Open the image file
    img = Image.open(image_path)
    
    # Resize image while keeping aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width)
    img = img.resize((width, new_height))

    # Convert the image to grayscale
    img = img.convert('L')

    # Define ASCII characters for different levels of brightness
    ascii_chars = '@%#*+=-:. '
    num_chars = len(ascii_chars)

    # Get the pixel data
    pixels = img.getdata()

    # Map the pixels to ASCII characters
    ascii_str = ''.join(ascii_chars[int(pixel / 255 * (num_chars - 1))] for pixel in pixels)
    
    # Split the string into lines of width
    ascii_str = '\n'.join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))
    
    # Write the ASCII art to a text file
    with open(output_file, 'w') as file:
        file.write(ascii_str)

# Usage example
image_to_ascii('ConsoleArt/ImageToAscii/bugatti.jpg', 'ConsoleArt/ImageToAscii/Output.txt', width=100)
