import visualkeras
from keras.models import load_model


model = load_model("/Users/dariabebin/PycharmProjects/BENorMONKE/models/finetuning.h5", compile=False)
visualkeras.layered_view(model, legend=True)  # without custom font

visualkeras.layered_view(model, legend=True).show()  # selected font

model.summary()