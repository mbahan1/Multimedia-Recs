from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('shows/', views.ShowList.as_view(), name="show-list"),
    path('shows/new/', views.Show_Create.as_view(), name="show_create"),
    path('shows/<int:pk>/', views.Show_Detail.as_view(), name="show_detail"),
    path('shows/<int:pk>/update', views.Show_Update.as_view(), name="show_update"),
    path('shows/<int:pk>/delete', views.Show_Delete.as_view(), name="show_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('reviews/', views.reviews_index, name='reviews_index'),
    path('reviews/<int:review_id>', views.reviews_show, name='reviews_show'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]