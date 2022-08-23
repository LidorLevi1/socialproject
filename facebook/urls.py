from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name="search"),
    path('signup/',views.signup_user,name="signup"),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name="logout"),
    path('profile/<str:username>',views.profile,name='profile'),
    path('profile/<str:username1>/friend',views.add_friend,name='add_friend'),
    path('profile/<str:username>/edit',views.edit_profile,name="editprofile"),
    path('profile/<str:username>/about',views.profile_about,name="profileabout"),
    path('profile/<str:username>/friends',views.profile_friends,name="profilefriends"),
    path('profile/<str:username>/remove',views.profile_remove,name="profileremove"),
    # path('profile/<str:username>/groups',views.edit_profile,name="editprofile"),
    path('post/<str:id>/add',views.addpost,name="addpost"),
    path('post/<str:id>',views.post,name="post"),
    path('post/<str:id>/likes',views.addlike,name="like_post"),
    path('post/<str:id>/editpost',views.edit_post,name="editpost"),
    path('post/<str:id>/remove',views.remove_post,name="removepost"),
    path('post/<str:id>/comment',views.addcomment,name="addcomment"),
    path('comment/<str:id>/remove',views.remove_comment,name="removecomment"),
    path('comment/<str:id>/edit',views.edit_comment,name="editcomment"),
    # path('group/',views.group),
    # path('newgroup/',views.new_group),
    # path('editgroup/',views.edit_group),
    # path('removegroup/',views.remove_group),
    

]