from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoints),
    path('advocates/', views.advocate_list, name= 'advocates'),
    # path('advocates/<str:username>', views.advoacte_details)
    path('advocates/<str:username>', views.AdvocateDetails.as_view()),

    path('companies/', views.Companies.as_view())
]
