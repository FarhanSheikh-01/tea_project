from django.shortcuts import render
from django.apps import apps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import numpy as np
import logging
import io

# Define views here
def home(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'introduction.html')

def tea_view(request):
    return render(request, 'composition.html')

def chemicals(request):
    return render(request, 'fertilizers.html')

def best_practice(request):
    return render(request, 'practices.html')


logger = logging.getLogger(__name__)
CLASS_NAMES = [
'Anthracnose',
 'red leaf spot',
 'healthy',
 'algal leaf',
 'brown blight',
 'bird eye spot',
 'white spot',
 'gray light']

@csrf_exempt
def predict_sickness(request):
    if request.method == 'POST':
        try:
            # Retrieve the uploaded image from the request
            image_file = request.FILES['image']
            image = Image.open(image_file).convert("RGB")  # Ensure the image is in RGB format

            # Preprocess the image
            image = image.resize((224, 224))  # Resize to match model input size
            image_array = np.array(image) / 255.0  # Normalize pixel values
            image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

            # Load the pre-trained model from AppConfig
            model = apps.get_app_config('myapp').model

            # Make a prediction
            predictions = model.predict(image_array)
            predicted_index = np.argmax(predictions)  # Get the index of the highest prediction
            predicted_class = CLASS_NAMES[predicted_index]  # Map the index to the class name
            confidence = np.max(predictions) * 100  # Calculate confidence

            # Return the prediction result
            return JsonResponse({
                'status': 'success',
                'result': predicted_class,
                'confidence': f'{confidence:.2f}%'
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})