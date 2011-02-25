from django.conf.urls.defaults import *
from rpc import Router

router = Router()

urlpatterns = patterns('nezabudka.views',
    url(r'^$', 'index', name='index'),
    url(r'^router/$', router, name='router'),
    url(r'^router/api/$', router.api, name='api'),       
)