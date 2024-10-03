from PIL import Image

def get_unique_colours(image_path):
    unique_pixels = []
    buffer = 16
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        pixels = img.getdata()
        for p in pixels:
            pixel_is_a_new_colour = True
            for up in unique_pixels:
                if p[0] <= up[0]+buffer and p[0] >= up[0]-buffer and p[1] <= up[1]+buffer and p[1] >= up[1]-buffer and p[2] <= up[2]+buffer and p[2] >= up[2]-buffer:
                    pixel_is_a_new_colour = False
                    break
            if pixel_is_a_new_colour:
                unique_pixels.append(p)
    return unique_pixels;

def read_message(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Could not read the file."

def encode_message(image_path, message, unique_colours):
    buffer = 16
    new_pixels = []
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        pixels = img.getdata()
        i = 0   # unique_colours index
        for p in pixels:
            if i < len(unique_colours) and p[0] <= unique_colours[i][0]+buffer and p[0] >= unique_colours[i][0]-buffer and p[1] <= unique_colours[i][1]+buffer and p[1] >= unique_colours[i][1]-buffer and p[2] <= unique_colours[i][2]+buffer and p[2] >= unique_colours[i][2]-buffer:
                new_pixels.append((0, 0, 0))
                print(message[i])
                i += 1
            else:
                new_pixels.append(p)

        new_img = Image.new("RGB", img.size)
        new_img.putdata(new_pixels)

        new_img.save("encoded_image.png")



image_path = 'test.png'
unique_colours = get_unique_colours(image_path)
print('total unique colours: ', len(unique_colours))

file_path = "message.txt"
message = read_message(file_path)
print('mesage length: ', len(message))

if (len(message) > len(unique_colours)):
    print('Error: cannot enocode the message. The message length:', len(message), 'exceeds the total unique colours:', len(unique_colours), 'in the image')
else:
    encode_message(image_path, message, unique_colours)











