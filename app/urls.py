from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'app.views.index'),
    url(r'^detail/(\d+)/$', 'app.views.detail')
]