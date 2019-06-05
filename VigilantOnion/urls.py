from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

app_name="VigilantOnion"

urlpatterns = [
	# Tratativa de url para o app usuários
    url(r'^', include('VigilantOnion.dashboard.urls', namespace='dashboard')),
    # Tratativa de Url para o app Admin
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
