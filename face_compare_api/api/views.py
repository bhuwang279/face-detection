# The future is now!
import uuid

import face_recognition
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
import os

from django.conf import settings


def upload_image(request):
    img = request.FILES['image']
    img_extension = os.path.splitext(img.name)[-1]
    # return path to saved image
    return default_storage.save(settings.MEDIA_URL + str(uuid.uuid4()) + img_extension, img)


def compare_images(self, *args, **kwargs):
    base_image_file  = kwargs.get("base_image")
    current_image_file = kwargs.get("current_image")

    base_face = face_recognition.load_image_file(base_image_file)
    base_face_encoding = face_recognition.face_encodings(base_face)[0]

    print(base_face_encoding)

    current_face = face_recognition.load_image_file(current_image_file)
    current_face_encoding = face_recognition.face_encodings(current_face)[0]

    results = face_recognition.compare_faces([base_face_encoding], current_face_encoding)

    print(results)

    return results[0]

class Image(APIView):

    def post(self, request, *args, **kwargs):

        result = compare_images(self,base_image=request.FILES['base_image'], current_image = request.FILES['current_image'])

        return Response({"success":result}, status=status.HTTP_202_ACCEPTED)