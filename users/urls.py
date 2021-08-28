from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views  
# from .views import(
#     PostDeleteView,
#     PostUpdateView,
#     PostDetailView,
#     UserPostListView,
# )

urlpatterns =[
    path('profile/', views.profile, name='profile'),

    # path('ss/',views.student_list, name='student_list'),
    path('', views.HomePage, name='homepage'),  
   
    # path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('signup/',views.signup_view,name='account_signup'),
    path('sent/', views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    path('login/', views.login_request,name='account_login'),
    path('logout/', views.logout_request, name='account_logout'),
    path('change/', views.password_change ,name='PasswordChangeForm'),

    path('password-reset/',
         views.PasswordResetView,name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    path('students',views.student, name='customer'),
    path('edit/', views.student_list,name='student_list'),  
    path('update/', views.update,name='update'),  
    path('delete/<int:id>', views.delete ,name='delete'),  
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
