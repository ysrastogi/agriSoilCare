from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.ph_prediction import ph_model
from core.k_prediction import k_model
from core.n_prediction import n_model
from core.p_prediction import p_model
from django.views import View
from PIL import Image
import numpy as np
import joblib
import cv2
import io


def handle_uploaded_image(image_file):
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    average_color_per_row = np.average(image, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    r = average_color[0]
    g = average_color[1]
    b = average_color [2]
    return r,g,b

@method_decorator(csrf_exempt, name='dispatch')
class pHAPI(View):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image', None)
        if image_file:
            r,g,b = handle_uploaded_image(image_file)
            rgb_data = (r,g,b)
            result = ph_model(rgb_data)
            return JsonResponse({'prediction': result}, safe=False)
        return JsonResponse({'error': 'No image provided'}, status=400)
    
@method_decorator(csrf_exempt, name='dispatch')
class kAPI(View):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image', None)
        if image_file:
            r,g,b = handle_uploaded_image(image_file)
            rgb_data = (r,g,b)
            result = k_model(rgb_data)
            return JsonResponse({'prediction': result}, safe=False)
        return JsonResponse({'error': 'No image provided'}, status=400)
    
@method_decorator(csrf_exempt, name='dispatch')
class pAPI(View):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image', None)
        if image_file:
            r,g,b = handle_uploaded_image(image_file)
            rgb_data = (r,g,b)
            result = p_model(rgb_data)
            return JsonResponse({'prediction': result}, safe=False)
        return JsonResponse({'error': 'No image provided'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class nAPI(View):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image', None)
        if image_file:
            r,g,b = handle_uploaded_image(image_file)
            rgb_data = (r,g,b)
            result = n_model(rgb_data)
            return JsonResponse({'prediction': result}, safe=False)
        return JsonResponse({'error': 'No image provided'}, status=400)

