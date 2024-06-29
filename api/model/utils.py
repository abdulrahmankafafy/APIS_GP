import os
import joblib
from fastai.vision.all import *


def predict_value(model_path, image_path):
    try:
        if not os.path.exists(model_path):
            raise ValueError(f"Model file '{model_path}' not found.")

        with open(model_path, 'rb') as f:
            learn_inf = joblib.load(f)

        if not os.path.exists(image_path):
            raise ValueError(f"Image file '{image_path}' not found.")

        new_image = PILImage.create(image_path)
        prediction, _, _ = learn_inf.predict(new_image)
        return str(prediction)

    except Exception as e:
        error_message = f"Error predicting value: {str(e)}"
        print(error_message)
        raise ValueError(error_message)

