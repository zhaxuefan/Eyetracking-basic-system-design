

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.vis_utils import plot_model


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'E:/人机交互/eyes/hahaha/xin/training',
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=2,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        'E:/人机交互/eyes/hahaha/xin/validationing',
        target_size=(150, 150),
        batch_size=2,
        class_mode='categorical')

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150,150,3)))

model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(9))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.fit_generator(
        train_generator,
        samples_per_epoch=200,
        nb_epoch=1,
        validation_data=validation_generator,
        nb_val_samples=80)

#model.save_weights('/home/liuying/interaction/first_try9class.h5')
plot_model(model, to_file='model1.png', show_shapes=True)
model_json = model.to_json()
with open("model9class.json", "w") as json_file:
    json_file.write(model_json)