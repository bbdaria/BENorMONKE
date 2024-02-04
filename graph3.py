import tkinter as tk
import tkinter.filedialog
import tensorflow as tf
from PIL import Image, ImageTk
from tensorflow.keras.preprocessing import image

# Load the models
model1 = tf.keras.models.load_model('models/works.sp')
model2 = tf.keras.models.load_model('models/transfered.h5')
model3 = tf.keras.models.load_model('models/finetuning.h5')

img_ref = None
# a list for the buttons
buttons = []

def preprocess_image(img_path):
    # loads the image and sizes it
    img = image.load_img(img_path, target_size=(256, 256)) #resize
    img_array = image.img_to_array(img) #convert to array
    img_array /= 255. #all values between 0 and 1
    return img_array

def perdiction_results(img_path, model):
    # calculates the prediction value
    image = tf.io.read_file(img_path)
    tensor = tf.io.decode_image(image, channels=3, dtype=tf.dtypes.uint8)
    tensor = tf.image.resize(tensor, [256, 256])
    input_tensor = tf.expand_dims(tensor, axis=0)
    results = model.predict(input_tensor)
    return results

def select_image():
    global img_ref, buttons
    # Destroy the previous buttons
    for b in buttons:
        b.destroy()

    img_path = tk.filedialog.askopenfilename()

    if img_path:
        # Display the image
        img_pil = Image.open(img_path)
        img_pil = img_pil.resize((400, 400))
        img_tk = ImageTk.PhotoImage(img_pil) #creates an image object
        label.config(image=img_tk)
        label.image = img_tk  # keep a reference to the image

        def show_prediction(network, network_name):
            # Create a new window to display the prediction
            prediction_window = tk.Toplevel()
            prediction_window.geometry('400x200')
            prediction_window.title('Prediction')
            # Get the prediction
            results = perdiction_results(img_path, network)

            conclusion = "Monkey"
            if results < 0.5:
                conclusion = "Ben"

            prediction_label = tk.Label(prediction_window,
                                        text=f'Prediction {network_name}: {results}\nConclusion: {conclusion}')
            prediction_label.pack()

        # Creates buttons for each network
        button1 = tk.Button(root, text='darias network', command=lambda: show_prediction(model1, "daria network"))
        button2 = tk.Button(root, text='transfer learning', command=lambda: show_prediction(model2, "transfer learning"))
        button3 = tk.Button(root, text='fine tuning', command=lambda: show_prediction(model3, "fine tuning"))

        button1.pack()
        button2.pack()
        button3.pack()

        # Store the buttons
        buttons.append(button1)
        buttons.append(button2)
        buttons.append(button3)

        # Store the image object
        img_ref = img_tk

root = tk.Tk()
root.geometry('600x525')
root.title('Image Selector')

# button for picking the picture
button = tk.Button(root, text='Select Image', command=select_image)
button.pack()

label = tk.Label(root)
label.pack()
root.mainloop()


