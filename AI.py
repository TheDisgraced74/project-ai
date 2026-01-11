import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import matplotlib.animation as matanim

# ---------------------------
# 1. Train or load MNIST model
# ---------------------------
def create_and_train_model():
    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Normalize and reshape
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    # Build a simple CNN
    model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=(28,28), name="Input1"),  
            tf.keras.layers.Flatten(name='Flatten1'),
            tf.keras.layers.Dense(512, activation=tf.nn.relu, name='Dense1'),
            tf.keras.layers.Dropout(0.2, name='Dropout1'),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax, name='Dense2')
            ])

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    print("Training model... This may take a minute.")
    model.fit(x_train, y_train, epochs=8, validation_data=(x_test, y_test))
    model.save("mnist_model.keras")
    return model

try:
    model = keras.models.load_model("mnist_model.keras")
    print("Loaded existing model.")
except:
    model = create_and_train_model()

# ---------------------------
# 2. Tkinter Drawing Interface
# ---------------------------
class MNISTApp:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("AI Digit Recognizer")

        self.canvas = tk.Canvas(root, width=280, height=280, bg="black")
        root.tk.call('tk','scaling',1.0)
        self.canvas.pack()

        self.image = Image.new("L", (280, 280), color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Predict", command=self.predict).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Clear", command=self.clear).pack(side=tk.LEFT)

        self.result_label = tk.Label(root, text="Draw a digit and click Predict" "\n"
        "Please draw then big as it is rescaled to 28x28 image", font=("Arial", 16))
        self.result_label.pack()

    def paint(self, event):
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        self.canvas.create_oval(x1, y1, x2, y2, fill="white", width=0)
        self.draw.ellipse([x1, y1, x2, y2], fill=0)
        
    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 280, 280], fill=255)
        self.result_label.config(text="Draw a digit and click Predict")

    def predict(self):
        # Resize to 28x28 and normalize
        img_resized = self.image.resize((28, 28))
        img_array = np.array(img_resized).astype("float32") / 255.0
        img_array = np.expand_dims(img_array, axis=(0, -1))

        prediction = self.model.predict(img_array.reshape(1,28,28))[0]
        digit = np.argmax(prediction)
        confidence = np.max(prediction)

        fig = plt.figure(figsize=(10,10))
        ax2 = fig.add_subplot(1,1,1)
        _ = ax2.bar(range(10), prediction*10, alpha=0.8, color='b')
        ax2.set_xticks(np.arange(10))
        ax2.set_xticklabels(range(10))
        ax2.set_title("Prediction Probability")

        ax2.set_yticks(range(0, 11))
        ax2.set_yticklabels([str(ri)+'%' for ri in range(0, 110, 10)])
        ax2.set_aspect(1.0)

        plt.tight_layout()
        plt.show()
        self.result_label.config()

# ---------------------------
# 3. Run the app
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MNISTApp(root, model)
    root.mainloop()