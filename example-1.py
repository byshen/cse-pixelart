from CSEPixelArt import *

def main():

    print("Example 1: a simple image")

    img = create_img(16,16,(255,255,255))
    count = 0
    for row in range(height(img)):
        for col in range(width(img)):
            count = count + 1
            if count % 3 == 0:
                img[row][col] = (0,0,0)

    print("Writing example-1.png")
    save_img(img, "example-1.png")
    print("Writing example-1-big.png")
    save_img(img, "example-1-big.png", 10)

main()