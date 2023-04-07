from PIL import Image
from io import BytesIO

with open('cat.jpg', 'rb') as f:
    data = f.read()
    print(data)

# создаем объект BytesIO для чтения байт-кода из переменной data
stream = BytesIO(data)

# открываем изображение при помощи метода Image.open()
image = Image.open(stream)
image.show()
# получаем размеры изображения
width, height = image.size
new_width = 500
new_height = int(height * new_width / width)
resized_image = image.resize((new_width, new_height))   # изменяем размер на новые значения ширины и высоты
black_and_white_image = resized_image.convert('L')  # применяем эффект "черно-белого" фильтра
output_stream = BytesIO()   # сохраняем обработанное изображение в объект BytesIO
black_and_white_image.save(output_stream, format='JPEG')

# получаем байт-код обработанного изображения
output_data = output_stream.getvalue()

# побайтово записываем новое изображение
with open('changed_cat_photo.jpeg', 'wb') as f:
    f.write(output_data)


