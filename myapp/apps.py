import logging
from django.apps import AppConfig
from joblib import load
import os
from django.conf import settings

# Configure logger
logger = logging.getLogger(__name__)

class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    def ready(self):
        try:
            # Construct the model path
            model_path = os.path.join(settings.BASE_DIR, "SaveModels", "tea_sickness_model_80.joblib")

            # Load the model if it exists
            if os.path.exists(model_path):
                self.model = load(model_path)
                logger.info("Model loaded successfully.")
            else:
                logger.error(f"Model not found at {model_path}")
                raise FileNotFoundError(f"Model file not found at {model_path}")
        except Exception as e:
            logger.exception("An error occurred while loading the model.")
            raise e
