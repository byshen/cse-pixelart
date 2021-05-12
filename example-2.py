from CSEPixelArt import *

def main():

    print("Example 2: a simple animation")

    h = 16
    w = 16
    anim = [create_img(h, w, (255,255,255))]
    for row in range(h):
        next_frame = copy_img(anim[-1]) # copy last frame
        for col in range(w):
            next_frame[row][col] = (255,0,0)
        anim.append(next_frame)

    print("Writing example-2.gif")
    save_anim(anim, "example-2.gif")
    print("Writing example-2-big.gif")
    save_anim(anim, "example-2-big.gif", 10)

main()