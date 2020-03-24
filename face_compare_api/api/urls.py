from django.conf.urls import url
from .views import Image, Register, Verify

urlpatterns = [
    url(r'^image/$', Image.as_view(), name='upload-image'),
    url(r'^register/$', Register.as_view(), name='register-image'),
    url(r'^verify/$', Verify.as_view(), name='register-image'),

]