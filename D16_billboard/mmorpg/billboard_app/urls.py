from django.urls import path
from .views import (
   AdvertisementsList, AdvertisementDetail, AdvertisementCreate, AdvertisementUpdate, AdvertisementDelete,
   AuthorAdvertisementsList, ResponseCreate, ResponseList, ResponseDetail, ResponseDelete, ResponseUpdate,
   CommentatorresponsesList, AdvertisementsResponsesList, Search
)


urlpatterns = [
    path("", AdvertisementsList.as_view(), name="advert-list"),
    path("advertisement_create/", AdvertisementCreate.as_view(), name="advertisement_create"),
    path("advertisements/<int:pk>/", AuthorAdvertisementsList.as_view(), name="author-list"),
    path("response_list/", ResponseList.as_view(), name="response-list"),
    path("response_create/<int:pk>/", ResponseCreate.as_view(), name="response-create"),
    path("advertisement_update/<int:pk>/", AdvertisementUpdate.as_view(), name="advertisement_update"),
    path("advertisement_delete/<int:pk>/", AdvertisementDelete.as_view(), name="advertisement_delete"),
    path("advertisement_detail/<int:pk>/", AdvertisementDetail.as_view(), name="advertisement_detail"),
    path('response_detail/<int:pk>/', ResponseDetail.as_view(), name='response_detail'),
    path('response_delete/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),
    path('response_edit/<int:pk>/', ResponseUpdate.as_view(), name='response_edit'),
    path('responses/commentator/<int:pk>/', CommentatorresponsesList.as_view(), name='commentator_list'),
    path('responses/advertisements/<int:pk>/', AdvertisementsResponsesList.as_view(), name='commentators_list'),
    path('search/', Search.as_view(), name='search'),
]