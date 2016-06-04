from PIL import Image, ImageOps
import sys

def extract_image(from_image, s=4):
    data = Image.open(from_image)
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x,y))
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s

            data.putpixel((x,y), (red, green, blue))
    return data

def hide_image(public_img, secret_img, s=4):
    data = Image.open(public_img)
    key  = ImageOps.autocontrast(Image.open(secret_img).resize(data.size))
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x, y))
            q = key.getpixel((x, y))
            red   = p[0] - (p[0] % s) + (s * q[0] / 255)
            green = p[1] - (p[1] % s) + (s * q[1] / 255)
            blue  = p[2] - (p[2] % s) + (s * q[2] / 255)

            data.putpixel((x,y) , (red, green, blue))
    return data

def give_help():
    print "Wrong, try!"
    print "%s show from.jpg" % sys.argv[0]
    print "%s hide public.jpg secret.jpg" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        give_help()
    elif sys.argv[1] == "show":
        extract_image(sys.argv[2]).save("extraced.png");
        print("Complete!\nImage saved as extracted.png");
    elif sys.argv[1] == "hide":
        hide_image(sys.argv[2],sys.argv[3]).save("hidden.png");
        print("Complete!\nHide the image");
    else:
        give_help()
