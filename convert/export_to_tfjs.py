import tensorflow as tf
import tensorflowjs as tfjs

model = tf.keras.models.load_model("gender_model.keras")

tfjs.converters.save_keras_model(gender_model, "tfjs_gender_model")
print("Модель успешно конвертирована в папку tfjs_gender_model")