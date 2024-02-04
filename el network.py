
import tensorflow as tf
import time as Time
from matplotlib import pyplot as plt

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

val_ds = image_dataset_from_directory(
        "dataset2",
        validation_split=0.2,
        subset="validation",
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


model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1. / 255, input_shape=(256, 256, 3)),
    tf.keras.layers.BatchNormalization(),

    tf.keras.layers.Conv2D(6, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.Conv2D(8, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.Conv2D(10, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()
model.compile(optimizer='Adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])
epochs = 5
tic = Time.time()

history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1,
            )


toc = Time.time()

# Calculate training time and format as min:sec
minutes = format((toc - tic) // 60, '.0f')
sec = format(100*((toc-tic) % 60)/60, '.0f')
print(f"Total training time (min:sec): {minutes}:{sec}")

# evaluating the model

print("Train accuracy: " + str(max(history.history['accuracy'])))
print("val_accuracy: " + str(max(history.history['val_accuracy'])))

# Print final loss and accuracy
loss, accuracy = model.evaluate(test_ds)
print("Final loss: {:.2f}".format(loss))
print("Final accuracy: {:.2f}%".format(accuracy * 100))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.title('learning curves')
plt.xlabel('epoch')
plt.ylabel('Loss (cross entropy)')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.legend()
plt.show()


# saving the model
name = input("please enter the name of the model\n")
model.save("models/" + name + ".h5")
print("Saved model to disk")


