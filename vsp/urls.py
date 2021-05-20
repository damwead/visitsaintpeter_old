from django.contrib import admin
from django.urls import path

from pages.views import about_view
from news.views import HomeView, EventView

# for image uploading to site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about_view),
    path('events/', EventView.as_view()),
    path('admin/', admin.site.urls),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
