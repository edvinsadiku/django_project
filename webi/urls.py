from django.urls import path
from django.contrib import admin
from .views import HomeView , PostimetView,ListaView,CategoryView,ContactView,document_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('publikimet/', ListaView.as_view(), name="ListaView"),
    path('publikimet/<int:pk>', PostimetView.as_view(), name="postimet"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('kontakti', ContactView.as_view(), name="ContactView"),
    path('materialepershkarkim', document_list, name="materiale"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
