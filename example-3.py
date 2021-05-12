from CSEPixelArt import *
import colorsys
import math

# The third example uses a different color representation called HSV,
# so we need a way to convert HSV to RBG
# See https://en.wikipedia.org/wiki/HSL_and_HSV
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def main():

    print("Example 3: a more complicated animation")

    h = 16
    w = 16
    total = h*w
    max_frames = 60
    skip = math.ceil(total / (max_frames - 1))
    frame = create_img(h, w, (255,255,255))
    anim = [frame]
    count = 0
    for row in range(h):
        for col in range(w):
            count = count + 1
            frame[row][col] = hsv2rgb(count / total, 1, 1)
            if count % skip == 0:
                anim.append(copy_img(frame))

    print("Writing example-3.gif")
    save_anim(anim, "example-3.gif")
    print("Writing example-3-big.gif")
    save_anim(anim, "example-3-big.gif", 10)

main()