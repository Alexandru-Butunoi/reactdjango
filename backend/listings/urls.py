from django.urls import path
from .views import ListingsView, ListingDetailView

urlpatterns = [
    path('', ListingsView.as_view()),
    path('<pk>/', ListingDetailView.as_view())
]
