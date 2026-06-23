from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view, RegisterView, Profileview

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view() , name='register'),
    path('profile/', Profileview.as_view() , name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)