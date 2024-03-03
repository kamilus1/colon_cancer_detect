from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

datagen_1 = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

datagen_2 = ImageDataGenerator(
        rotation_range=60,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
 
datagen_3 = ImageDataGenerator(
        rotation_range=60,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        vertical_flip=True,
        fill_mode='nearest')
datagen_4 = ImageDataGenerator(
        rotation_range=90,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

datagen_5 = ImageDataGenerator(
        rotation_range=120,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
def generate(data_generator: ImageDataGenerator, quantity = 3):
    
    for item in os.listdir("v_data/train/clean"):
        image_path = f"v_data/train/clean/{item}"
        img = load_img(image_path)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in data_generator.flow(x, batch_size=1, save_to_dir="preview", save_prefix="clean", save_format="jpeg"):
            i += 1
            if i > quantity:
                break
generate(datagen_1)
generate(datagen_2)
generate(datagen_3)
generate(datagen_4)
generate(datagen_5)