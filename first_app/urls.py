from django.urls import path
from . import views
urlpatterns = [
	path('', views.home),
	path('home', views.home),
	path('register', views.register),
	path('create_user', views.create_user),
	path('login', views.login), 	
	path('logout', views.logout), 
	path('profile/<int:user_id>', views.profile),
	path('update_bio/<int:user_id>', views.update_bio),
	path('delete_photo/<int:user_id>', views.delete_photo),
	path('user_profile/<int:user_id>', views.user_profile, name="user_profile"),
	path('messageboard', views.messageboard),
	path('create_message', views.create_message),
	path('post_message', views.post_message),
	path('post_comment/<int:user_id>', views.post_comment), 
	path('delete_message/<int:message_id>', views.delete_message, name="delete_message"),
	path('quiz', views.quiz),
	path('trail_family', views.trail_family),
	path('fam_results', views.fam_results),
	path('update_photo/<int:user_id>', views.update_photo),


]