import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout,LeakyReLU

def make_model():
    transfer = tf.keras.applications.EfficientNetB4(
              input_shape=(300,300,3),
              include_top=False,
              weights='imagenet',
)
    transfer.trainable = False
    # transfer.summary()

    model = tf.keras.models.Sequential([
    transfer,
    tf.keras.layers.GlobalAveragePooling2D(),
    #Flatten
    tf.keras.layers.Flatten(),
    
    # Fully
    tf.keras.layers.Dense(1280, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'), 
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(5, activation='softmax')
])
    
    return model