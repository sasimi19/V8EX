from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'app.views.index'),
    url(r'^index/$', 'app.views.index'),
    url(r'^detail/(\d+)/$', 'app.views.detail'),
    url(r'^reg/$', 'app.views.reg'),
    url(r'^login/$', 'app.views.login')
]