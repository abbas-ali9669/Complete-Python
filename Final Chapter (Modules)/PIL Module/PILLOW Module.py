# In this topic we will learn about PILLOW Module. That how we can edit images using modules
# we will learn about
# 1. Change the image extension
# 2. Reize image file
# 3. resize multiple image using for loop
# 4. Sharpness
# 5. Brightness
# 6. Color
# 7. Contrast
# 8. Image Blur, Gaussian Blur


from PIL import Image, ImageEnhance, ImageFilter
import os

# img = Image.open(r"D:\Business Work\For Fiverr\Gig Fotos\web designing food website.png")
# img.save("web designing food website.pdf")

# 1. Change the image extension
# img1 = Image.open("dog2.jpg")    # Here we will open our image
# img1.save("dog1.png")    # This is for image saving. Now if we want just to see the picture then we can use show() funtion
# img1.show()    # Yhis functon will judt show th picture


# 2. Reize image file.
# size = (250,250)
# img1.thumbnail(size)
# img1.show()


# 3. resize multiple image using for loop
# for item in os.listdir():
#     if item.endswith(".jpg"):
#         img = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img.save(f"{filename}.png")


# 4. Sharpness
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(10).save("Dogedited.jpg")
# Input:
# 0 -> Blurry
# 1 -> Original Image
# 2 or more -> Image with increase Sharpness
# We can also pass center num like, 1.5, 2.7 etc


# 5. Brightness
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1).save('Bright.jpg')


# 6. Color
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save("color.jpg")


# 7. Contrast
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(100).save("contrast.jpg")


# 8. For Blur Image, We use Class Gaussian Blur
# img1.filter(ImageFilter.GaussianBlur(radius=5)).save("gblur.jpg")



# 9. Resizing Multiple images (own)
# for item in os.listdir():
#     if item.endswith(".jpg"):
#         img = Image.open(item)
#         size = (250,250)
#         img.thumbnail(size)
#         file, extension = os.path.splitext(item)
#         img.save(f"{file}.png")
