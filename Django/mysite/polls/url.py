from django.urls import converters, path, register_converter, re_path
from django.urls.resolvers import URLPattern
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# urlpatterns = [
#     # path('', views.index, name ='index'),
#     # path('<yyyy:year>/', views.custom_path)
#     # re_path(r'^(?P<year>[0-9]{4})/$', views.custom_path, {'name': 'hau'}),
    
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
