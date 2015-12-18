from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'app.views.index'),
    url(r'^index/$', 'app.views.index'),
    url(r'^detail/(\d+)/$', 'app.views.detail'),
    url(r'^reg/$', 'app.views.reg'),
    url(r'^login/$', 'app.views.login'),
    url(r'logout/$', 'app.views.logout'),
    url(r'reply/(\d+)$', 'app.views.reply'),
    url(r'user/$', 'app.views.user'),
    url(r'post/$', 'app.views.post')
]