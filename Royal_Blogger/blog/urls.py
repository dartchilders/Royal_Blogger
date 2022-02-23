from django.urls import path
from .views import Home, PostDetail, AddPost, EditPost, DeletePost, Like
# from .views import BlogCategory, AddCategory

app_name = 'blog'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', PostDetail.as_view(), name='detail'),
    path('addpost/', AddPost.as_view(), name='add'),
    path('edit/article/<int:pk>', EditPost.as_view(), name='edit'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('like/<int:pk>', Like, name='likepost')
    # path('addcategory/', AddCategory.as_view(), name='addcategory'),
    # path('category/<str:cats>', BlogCategory, name='category'),
]