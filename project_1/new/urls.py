from django.urls import path
from new.views import NewsList, NewsDetail, NewsCrate, NewsUpdate,NewsDelete

urlpatterns=[
    path('', NewsList.as_view(), name='new'),
    path('<int:pk>/', NewsDetail.as_view(), name='detail'),
    path('create/',NewsCrate.as_view(), name='create' ),
    path('<int:pk>/update/',NewsUpdate.as_view(),name='update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='delete'),
    
    
]