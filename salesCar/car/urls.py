from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailsView.as_view(), name="details"),
    path('buy-car/<int:id>/', views.BuyCarView.as_view(), name="buy-car"),
    path('comment/<int:id>/', views.DetailsView.as_view(), name='add-comment')
]
