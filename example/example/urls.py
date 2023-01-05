from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.contrib.staticfiles import views

from tester.views import TestModelFormView, TestModelDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tester/create/', TestModelFormView.as_view(), name='create'),
    path('tester/<int:pk>/', TestModelDetailView.as_view(), name='detail'),
]


if settings.DEBUG:
    from django.urls import re_path

    urlpatterns += [re_path(r'^static/(?P<path>.*)$', views.serve)]
