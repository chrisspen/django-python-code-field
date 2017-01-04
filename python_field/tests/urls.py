
from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('python_field.tests.views',
    (r'^admin/', include(admin.site.urls)),
)
