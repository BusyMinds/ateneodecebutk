from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
# from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    patterns('',
        url(r'^$', 'ateneodecebutk.views.index', name='index'),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^gradebook/', include('gradebook.urls')),
        url(r'^downloads/', include('downloads.urls')),
    )
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
