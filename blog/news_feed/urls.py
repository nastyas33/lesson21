from django.urls import path
from .endpoints import PageListAPIView, PageCreateAPIView, PageListCreateAPIView, \
    PageUpdateAPIView, PageRetrieveUpdateAPIView, PageRetrieveDestroyAPIView, \
    PageRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('page-list/', PageListAPIView.as_view(), name="page_list"),
    path('page-create/', PageCreateAPIView.as_view(), name="page_create"),
    path('page-list-create/', PageListCreateAPIView.as_view(), name="page_list_create"),
    path('page-update/<int:pk>', PageUpdateAPIView.as_view(), name="page_update"),
    path('page-detail-update/<int:pk>', PageRetrieveUpdateAPIView.as_view(), name="page_retrieve_update"),
    path('page-retrieve-destroy/<int:pk>', PageRetrieveDestroyAPIView.as_view(), name="page_retrieve_destroy"),
    path('page-retrieve-update-destroy/<int:pk>', PageRetrieveUpdateDestroyAPIView.as_view(), name="page_retrieve_update_destroy"),

]