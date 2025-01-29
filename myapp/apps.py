import logging
from django.apps import AppConfig
import os
from django.conf import settings
from tensorflow.keras.models import load_model

# Configure logger
logger = logging.getLogger(__name__)

class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    def ready(self):
        try:
            # Construct the model path
            model_path = os.path.join(settings.BASE_DIR, "SaveModels", "tea_sickness_model.h5")

            # Load the model if it exists
            if os.path.exists(model_path):
                self.model = load_model(model_path)  # Load Keras model
                logger.info("Keras model loaded successfully.")
            else:
                logger.error(f"Model not found at {model_path}")
                raise FileNotFoundError(f"Model file not found at {model_path}")
        except Exception as e:
            logger.exception("An error occurred while loading the model.")
            raise e
