from PIL import Image, ImageFilter, ImageChops, ImageOps, ImageEnhance

# invert color, maximize contrast, sharpen edges, desaturate
def optimizeImage(img):
    optimizedImg = img
    optimizedImg = ImageChops.invert(optimizedImg) #comment this out to use ASCII as shadows
    enhancer = ImageEnhance.Contrast(optimizedImg)
    optimizedImg = enhancer.enhance(2)
    optimizedImg = optimizedImg.filter(ImageFilter.SHARPEN)
    optimizedImg = ImageOps.grayscale(optimizedImg)
    return optimizedImg