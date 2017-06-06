from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TodayTrendListView.as_view(), name='todaytrend-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.OneItemListView.as_view(), name='oneitem-list'),
]