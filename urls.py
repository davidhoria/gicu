from django.conf.urls.defaults import *
from gicu.views import *

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^index.html/$', informatii),
    ('^informatii.html/$', informatii),
)