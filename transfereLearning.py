

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import tensorflow as tf
import time as Time
from keras.applications import Xception
from tensorflow.keras.preprocessing import image_dataset_from_directory

image_size = (256, 256)
batch_size = 128


train_ds = image_dataset_from_directory(
        "dataset2",
        validation_split=0.2,
        subset="training",
        seed=123,
        color_mode="rgb",
        image_size=image_size,
        batch_size=batch_size
    )

test_ds = image_dataset_from_directory(
        "dataset2",
        validation_split=0.2,
        subset="validation",
        seed=123,
        color_mode="rgb",
        image_size=image_size,
        batch_size=batch_size
    )

base_model = Xception(
    weights='imagenet',
    input_shape=(256, 256, 3),
    include_top=False)

base_model.trainable = False
model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1. / 255, input_shape=(256, 256, 3)),
    base_model,
    tf.keras.layers.BatchNormalization(),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.summary()
model.compile(optimizer='Adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])

epochs = 1
tic = Time.time()
history = model.fit(
            train_ds,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1,
            )


toc = Time.time()

# Calculate training time and format as min:sec
minutes = format((toc-tic)//60, '.0f')
sec = format(100*((toc-tic) % 60)/60, '.0f')
print(f"Total training time (min:sec): {minutes}:{sec}")


# -----------------------------------------------------------------------

# evaluating the model

print("Train accuracy: " + str(max(history.history['accuracy'])))

# Print final loss and accuracy
loss, accuracy = model.evaluate(test_ds)
print("Final loss: {:.2f}".format(loss))
print("Final accuracy: {:.2f}%".format(accuracy * 100))

# saving the model
name = input("please enter the name of the model\n")
model.save("models/" + name + ".h5")
print("Saved model to disk")


