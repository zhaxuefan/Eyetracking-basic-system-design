import os

os.environ['CUDA_VISIBLE_DEVICES'] = '2'
from keras.models import model_from_json
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import keras
import numpy as np
datagen = ImageDataGenerator(rescale=1./255)


generator = datagen.flow_from_directory(
        '/home/liuying/interaction/train1',
        target_size=(150, 150),
        batch_size=2,
        class_mode=None,
        shuffle=False)


generator = datagen.flow_from_directory(
        '/home/liuying/interaction/validation1',
        target_size=(150, 150),
        batch_size=2,
        class_mode=None,
        shuffle=False)

#model = Sequential()
model.load_weights('/home/liuying/interaction/first_try.h5')


bottleneck_features_train = model.predict_generator(generator, 200)

np.save(open('bottleneck_features_train.npy', 'w'), bottleneck_features_train)

bottleneck_features_validation = model.predict_generator(generator, 20)

np.save(open('bottleneck_features_validation.npy', 'w'), bottleneck_features_validation)
train_data = np.load(open('bottleneck_features_train.npy'))
# the features were saved in order, so recreating the labels is easy
train_labels = np.array([0] * 10 + [1] * 10+ [2] * 10 + [3] * 10 + [4] * 10)

validation_data = np.load(open('bottleneck_features_validation.npy'))
validation_labels = np.array([0] * 4+ [1] * 4+ [2] * 4 + [3] * 4 + [4] * 4)


train_labels = keras.utils.to_categorical(train_labels, 5)
validation_labels = keras.utils.to_categorical(validation_labels, 5)


model = Sequential()
#train_data.shape[1:]
model.add(Flatten(input_shape=(4,4,512)))# 4*4*512
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
#model.add(Dense(1, activation='sigmoid'))
model.add(Dense(5, activation='softmax'))
#model.add(Dense(1))
#model.add(Dense(5))
#model.add(Activation('softmax'))


model.compile(loss='categorical_crossentropy',

              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(train_data, train_labels,
          nb_epoch=20, batch_size=2,
          validation_data=(validation_data, validation_labels))
