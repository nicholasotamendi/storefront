from django.views.generic import TemplateView
from django.urls import include, path 


#urlconf module

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'core/index.html'), name = 'api-home'),
    path('docs/', TemplateView.as_view(template_name = 'core/docs.html'), name = 'api-docs')
]
