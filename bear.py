from CSEPixelArt import *

def main():

    print("Example 4: example that loads an existing image file")

    cat = load_img("hawkinson.jpeg", (16,16))
    cat_laser_eyes = copy_img(cat)
    neon_green = (57, 255, 20)
    cat_laser_eyes[8][5] = neon_green
    cat_laser_eyes[8][6] = neon_green
    cat_laser_eyes[7][10] = neon_green
    cat_laser_eyes[7][11] = neon_green
    anim = [cat, cat]

    print("Writing bear.gif")
    save_anim(anim, "bear.gif", duration=300)
    print("Writing bear-big.gif")
    save_anim(anim, "bear-big.gif", scale=10, duration=300)


def scale(fname):
    print("Example 4: example that loads an existing image file")

    cat = load_img(fname, (16,16))
    anim = [cat, cat]

    print("Writing bear.gif")
    save_anim(anim, fname + ".png", duration=300)
    print("Writing bear-big.gif")
    save_anim(anim, fname+"x10.png", scale=10, duration=300)
# main()

def merge(files):
    anim = [load_img(fname, (16,16)) for fname in files]
    print("Writing bear.gif")
    save_anim(anim, "bear-all.gif", duration=500)
    print("Writing bear-big.gif")
    save_anim(anim, "bear-allx10.gif", scale=10, duration=500)


# scale("pixil-frame-0-2.png")
# scale("pixil-frame-0-bear-rainbowout.png")
# scale("pixil-frame-0-bear-rainbowall.png")

# scale("bear-plain.png")

files = ["bear-plain.png",  "bear-rainbowout.png", "bear-rainbowinside.png", "bear-rainbowall.png"]
merge(files)