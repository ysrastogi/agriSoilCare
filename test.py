from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

class ImageModelAPITest(TestCase):
    def test_image_upload(self):
        url = reverse('pHmodel')
        with open('experiments/test_image.jpg', 'rb') as img:
            image = SimpleUploadedFile(name='experiments/test_image.jpg', content=img.read(), content_type='image/jpeg')
            response = self.client.post(url, {'image': image}, format='multipart')
            self.assertEqual(response.status_code, 200)
            self.assertIn('prediction', response.json())
