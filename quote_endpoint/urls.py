from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pct_change_view', views.pct_change_view, name='pct_change_view'),
    path('query_equity', views.query_equity, name='query_equity'),
    path('detail_query', views.detail_query, name='detail_query'),
]
