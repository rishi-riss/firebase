"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from .login_veiw import login_view
from .fireconnect import fireconnect
from uploader import IndexView,SubmitView
from .upload import upload_to_firebase
from views import get_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('login/db/',fireconnect,name='db'),
    path('next/',upload_to_firebase,name='urls'),
    path('get/',get_image,name='image_nameS'),
    path('', IndexView.as_view(), name='index'),
    path('submit/', SubmitView.as_view(), name='submit'),

]

