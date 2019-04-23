from PIL import Image

img = Image.open('1.jpg')
w, h = img.size
print('Orginal size: %s, %s' % (w, h))
img.thumbnail((w // 2, h // 2))
print('Resize: %s, %s' % (w, h))
img.save('thumbnail.jpg', 'jpeg')