from face_compare_api.face_compare_api.api.celery_app import app
import face_recognition


@app.task(bind=True, name='compare_images')
def compare_images(self, *args, **kwargs):
    base_image_file  = kwargs.get("base_image")
    current_image_file = kwargs.get("current_image")

    base_face = face_recognition.load_image_file(base_image_file)
    base_face_encoding = face_recognition.face_encodings(base_face)[0]

    print(base_face_encoding)

    current_face = face_recognition.load_image_file(current_image_file)
    current_face_encoding = face_recognition.face_encodings(current_face)[0]

    results = face_recognition.compare_faces([base_face_encoding], current_face_encoding)

    return results[0]