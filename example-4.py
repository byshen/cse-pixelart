from CSEPixelArt import *

def main():

    print("Example 4: example that loads an existing image file")

    cat = load_img("cat.jpg", (16,16))
    cat_laser_eyes = copy_img(cat)
    neon_green = (57, 255, 20)
    cat_laser_eyes[8][5] = neon_green
    cat_laser_eyes[8][6] = neon_green
    cat_laser_eyes[7][10] = neon_green
    cat_laser_eyes[7][11] = neon_green
    anim = [cat, cat_laser_eyes]

    print("Writing example-4.gif")
    save_anim(anim, "example-4.gif", duration=300)
    print("Writing example-4-big.gif")
    save_anim(anim, "example-4-big.gif", scale=10, duration=300)

main()