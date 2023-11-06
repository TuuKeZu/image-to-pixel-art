from PIL import Image
from collections import Counter

SIZE = 7
file = "input/3.png"

def main():
    img = Image.open(file)
    out = Image.new("RGB", img.size)

    (w, h) = img.size

    gw = w // SIZE
    gh = h // SIZE


    for a in range(0, gw):

        for b in range(0, gh):

            rgb_list = []
            for i in range(0, SIZE):
                for j in range(0, SIZE):
                    wi = (a * SIZE) + i
                    hi = (b * SIZE) + j
                    rgb = img.getpixel((wi, hi))
                    rgb_list.append(rgb)
            
            map = Counter(rgb_list)
            
            for i in range(0, SIZE):

                for j in range(0, SIZE):
                    wi = (a * SIZE) + i
                    hi = (b * SIZE) + j

                    out.putpixel((wi, hi), map.most_common(1)[0][0])
            
    out.save("output/output.png")
                    

main()