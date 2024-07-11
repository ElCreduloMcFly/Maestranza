from django.urls import path
from .views import chequeo_email

urlpatterns = [
    path('chequeoemail/', chequeo_email, name='chequeoemail'),
]
