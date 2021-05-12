"""
This is a simple library to manipulate images. It allows you to create Pixel Art
programmatically. The focus on this library is not efficiency but
on ease of use. Users of this library need only know the Python concepts
covered in the first 6 weeks of CSE 8A.

The data format is as follows. An image is a list of rows; a row is a list of
pixels; a pixel a tuple of three integers, representing the Red, Green and Blue
components. The integers should be in the range 0 to 255.

For example the following is a 4x4 red/blue checkered pattern:

red = (255,0,0)
blue = (0,0,255)

checkered_img = 
  [[red,  blue, red,  blue],
   [blue, red,  blue, red],
   [red,  blue, red,  blue],
   [blue, red,  blue, red]]

Because an image is a list of rows, if you want to access the pixel at row R and
column C of an image IMG, you would use IMG[R][C].

The height of an image is the nuber of rows in it. The width of an image is the
number of columns, which is the number of pixels in a row. All rows need to have
the same number of pixels.

There are functions in this library to create blank images, copy images, load
images from various images formats, and save images to PNG format, and save a
list of images to an animated GIF format.

The functions in this library are:
  load_img: loads an image from disk
  load_anim: loads an animated image from disk (eg: animated GIF)
  create_img: creates an empty image
  copy_img: copies an image
  height: returns the height of an image (number of rows)
  width: returns the width of an image (number of columns)
  save_img: saves an image to disk as a PNG file
  save_anim: saves a list of images to disk as an animated GIF file
"""

import numpy as np
from PIL import Image

def load_img(filename, size = None, resample_filter = Image.LANCZOS):
    """
    Loads an image from a file, optionally resizes it and returns it in the
    CSEPixelArt image format (list of lists of pixels)

    PARAMS/RETURN

    filename: File name as a string. Many different formats are supported,
    including standard ones like JPEG, PNG, GIF.

    size: Requested size in pixels, as a 2-tuple: (width, height). If size is
    None or not provided, then no resizing is done.

    resample_filter: Optional resample filter to be used if resizing. The
    default is CSEPixelArt.Image.LANCZOS. For details on possible filters, see:
    https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters

    returns: An image as a list of lists of pixels. If the loaded file
    is an animated GIF, only returns the first animation frame. 

    EXAMPLE USES

    from CSEPixelArt import *

    # loads an image without resizing
    img = load_img("foo.jpg")

    # loads an image and resizes it to 16x16, using the default
    # LANCZOS resampling filter
    img = load_img("foo.jpg", (16,16))

    # loads an image and resizes it to 16x16, using the BILINEAR
    # resampling filter
    img = load_img("foo.jpg", (16,16), Image.BILINEAR)

    # loads an image and then loads it again,
    # resizing it to a width of 32, with proportional height
    img_full = load_img("foo.jpg")
    h = height(img_full)
    w = width(img_full)
    new_width = 32
    new_height =  int(h * (new_width/w))
    img_scaled = load_img("foo.jpg", (new_width, new_height))

    """
    pil_img = Image.open(filename)
    return pil_to_pixart(pil_img, size, resample_filter)

def load_anim(filename, size = None, resample_filter = Image.LANCZOS):
    """
    Loads an animation from a animated image file format (for example an
    animated GIF), optionally resizes each image in the animation and returns
    the animation as a list of images in the CSEPixelArt image format.

    For the parameters see the load_img function description.

    If the provided filename refers to a file that has a single image (e.g.: a
    JPEG file, or a non-animated GIF file), the returned list will have a single
    element in it.
    """
    pil_img = Image.open(filename)

    is_animated = getattr(pil_img, "is_animated", False)

    if is_animated:
        result = []
        for i in range(pil_img.n_frames):
            pil_img.seek(i)
            result.append(pil_to_pixart(pil_img, size, resample_filter))
        return result
    else:
        return [pil_to_pixart(pil_img, size, resample_filter)]

def create_img(height, width, color):
    """
    Creates an image of the given height/width filled with the given color
    
    PARAMS/RETURN

    height: Height of the image to be created, as an integer

    width: Width of the image to be created, as an integer

    color: RGB pixel as a tuple of 3 integers

    returns: An image as a list of lists of pixels

    EXAMPLE USES

    from CSEPixelArt import *

    # Create a 16x16 image filled with white pixels
    img = create_img(16,16,(255,255,255))

    """
    result = [None] * height
    for i in range(len(result)):
        result[i] = [color] * width
    return result

def copy_img(img):
    """
    Returns copy of the provided image

    EXAMPLE USES

    from CSEPixelArt import *

    # Return new image where red filter is applied 
    # to the provided image, on even rows, thus 
    # creating a red stripe effect.
    def red_filter_stripes(img):
        red_img = copy_img(img)
        for r in range(height(img)):
            if r % 2 == 0:
                for c in range(width(img)):
                    pix = red_img[r][c]
                    red_img[r][c] = (pix[0],0,0)
        return red_img

    """
    return [[pix for pix in row] for row in img]

def height(img):
    """
    Returns the number of rows in the image
    """
    return len(img)

def width(img):
    """
    Returns the number of columns in the image
    """
    return len(img[0])

def pil_to_pixart(pil_img, size = None, resample_filter = Image.LANCZOS):
    """
    THIS IS A PRIVATE FUNCTION: no need to use this function from the outside     

    Convert a Pillow image to an image in CSEPixelArt library format (which is a list
    of lists of pixels)
    """
    if size != None:
        pil_img = pil_img.resize(size, resample = resample_filter)

    # Convert to RGB format, if it's not already in the format
    pil_img = pil_img.convert("RGB")
    
    # Convert to Numpy 3D array, height by width by 3 
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)

    # Convert to a list of list of tuples. This removes all numpy arrays to make
    # it easier for clients of the library to manipulate the data (it also makes
    # things slower, but for small images it's not a problem)
    img = [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]

    return img

def pixart_to_pil(img, scale = 1):
    """
    THIS IS A PRIVATE FUNCTION: no need to use this function from the outside    

    Convert an image in CSEPixelArt library format (which is a list of lists of
    pixels) to a Pillow image. This only supports scaling up (ie: scale >= 1).
    """
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    if (scale > 1):
        pil_img = pil_img.resize((pil_img.width*scale, pil_img.height*scale), resample = Image.BOX)
    return pil_img

def save_img(img, filename, scale = 1):
    """
    Save the provided image to a file in PNG format

    PARAMS/RETURN

    img: Image to save. The image needs to be in the CSEPixelArt image format
    (list of lists of pixels)

    filename: Name of the file as a string. Note that the file will be saved in
    PNG format, no matter what file name you give. We save in PNG instead of GIF
    because PNG can support the full gamit of RGB colors expressible in our
    format (as opposed to GIF which can only support a maximum of 256 color)

    scale: Optional scale as an integer >= 1. Each pixel in img is turned into a
    scale by scale square in the saved image.

    returns: nothing

    """
    if height(img) * scale > 1000:
        print("WARNING: the height will be larger than 1000 pixels")
        print("This is unusual for this Pixel Art competition so it may be a bug")
    if width(img) * scale > 1000:
        print("WARNING: the width will be larger than 1000 pixels")
        print("This is unusual for this Pixel Art competition so it may be a bug")
    pil_img = pixart_to_pil(img, scale)
    pil_img.save(filename, format='png')


def save_anim(imgs, filename, scale = 1, duration = 100):
    """
    Save the provided animation to an animated GIF format.

    PARAMS/RETURN

    imgs: Animation to save. The animation is a list of "frames", where each
    frame is an image in the CSEPixelArt image format. For the CSE Pixel Art
    competition, there is a limit of 60 frames (this is the limit on the Divoom
    devices we will use to display some of the winners).

    filename: Name of the file as a string. Note that the file will be saved in
    GIF format, no matter what file name you give. The GIF format only supports
    256 colors per animation frame. If you use more than than in a given frame,
    the system will transform your frame to reduce the colors to 256 (which will
    lead to some visual artifacts). Note that if you are using 16x16 images, you
    are guaranteed to never use too many colors.

    scale: Optional scale as an integer >= 1. Each pixel in each frame is turned
    into a scale by scale square in the saved animation. The default for scale
    is 1.

    duration: Optional pause between frames, in milliseconds. The default is
    100.

    returns: nothing
    """
    if len(imgs) > 60:
        print("WARNING: the CSE Pixel Art Competition has a limit of 60 frames")
        print("Your animation has " + str(len(imgs)) + " frames")
    if height(imgs[0]) * scale > 1000:
        print("WARNING: the height will be larger than 1000 pixels")
        print("This is unusual for this Pixel Art competition so it may be a bug")
    if width(imgs[0]) * scale > 1000:
        print("WARNING: the width will be larger than 1000 pixels")
        print("This is unusual for this Pixel Art competition so it may be a bug")

    pil_imgs = [pixart_to_pil(x, scale).convert("P", palette = Image.ADAPTIVE) for x in imgs]
    pil_imgs[0].save(filename,  format='gif',
					save_all=True, append_images=pil_imgs[1:], optimize=False, duration=duration, loop=0)


