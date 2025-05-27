from PIL import Image

def hide_data(image_path, data, output_path):
    try:
        image = Image.open(image_path)
        pixels = list(image.getdata())

        binary_data = ''.join(format(ord(char), '08b') for char in data) + '00000000'

        if len(binary_data) > len(pixels) * 3:
            raise ValueError("The image is too small to hide the data.")

        pixel_index = 0
        new_pixels = []
        for pixel in pixels:
            new_pixel = []
            for channel in pixel[:3]:  
                if pixel_index < len(binary_data):
                    new_pixel.append((channel & ~1) | int(binary_data[pixel_index]))
                    pixel_index += 1
                else:
                    new_pixel.append(channel)
            
            if len(pixel) == 4:  
                new_pixel.append(pixel[3])
            new_pixels.append(tuple(new_pixel))

        new_image = Image.new(image.mode, image.size)
        new_image.putdata(new_pixels)
        new_image.save(output_path)
        print(f"Data successfully hidden in '{output_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


# image_path = "" 
# data = "" 
# output_path = "output.png"  
# def Call_Hide():