from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def home(request):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),	
		}
		return render(request, "home.html", context)
	else:
		return render(request, "home.html")

def register(request):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),	
		}
		return render(request, "registration.html", context)
	else:
		return render(request, "registration.html")

def create_user(request):
	if request.method == 'POST':
		errors = User.objects.basic_validator(request.POST)
		if errors:
			for key, value in errors.items():
				messages.error(request, value)
			print('error found')
			return redirect('/register')
		else:
			hashedpw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
			print(request.POST['password'])
			print(hashedpw)
			new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], email = request.POST['email'], password= hashedpw)
			request.session['User'] = new_user.id
			return redirect('/profile') 
	else: 
		redirect('/')

def login(request):
	if request.method == 'POST':
		errors = User.objects.login_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			return redirect('/register')
		else:
			logged_User = User.objects.get(username=request.POST['login_username'])
			request.session['User'] = logged_User.id
			return redirect(f'/profile/{logged_User.id}')
	else:
		redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def profile(request, user_id):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),
			"user_bio": Bio.objects.get(uploaded_by = User.objects.get(id=request.session['User']))
			}
		return render(request, 'profile.html', context)
	else: 
		print('user must be logged in')
		return redirect('/register')

def update_bio(request, user_id):
	if request.method == 'POST':
		logged_User = User.objects.get(id=request.session['User'])
		user_bio= Bio.objects.get(uploaded_by=request.session['User'])
		user_bio.location = request.POST['location']
		user_bio.fav_hike = request.POST['fav_hike']
		user_bio.bucket_list = request.POST['bucket_list']
		user_bio.snack = request.POST['snack']
		user_bio.hike_need = request.POST['hike_need']
		# user_bio.profile_pic = request.FILES['profile_pic']
		user_bio.save()
		print(user_bio.location)
		return redirect(f'/profile/{logged_User.id}')

def update_photo(request,user_id):
	if request.method == 'POST':
		logged_User = User.objects.get(id=request.session['User'])
		user_bio= Bio.objects.get(uploaded_by=request.session['User'])
		user_bio.profile_pic = request.FILES['profile_pic']	
		user_bio.profilpic.save()
	return redirect(f'/profile/{logged_User.id}')	

def delete_photo(request, user_id):
	if request.method == 'POST':
		logged_User = User.objects.get(id=request.session['User'])
		user_bio= Bio.objects.get(uploaded_by=request.session['User'])
		user_bio.profile_pic = user_bio(request.FILES['profile_pic'])
		user_bio.profile_pic.delete()
		user_bio.profile_pic.save()
		return redirect(f'/profile/{logged_User.id}')	

def user_profile(request, user_id):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),
			"user_bio": Bio.objects.get(uploaded_by = User.objects.get(id=request.session['User'])),
			"one_user": User.objects.get(id=user_id),
			"all_users": User.objects.all(), 
			"all_bios": Bio.objects.all(),
			}
		return render(request, 'user_profile.html', context)

def messageboard (request):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),
			"user_bio": Bio.objects.get(uploaded_by = User.objects.get(id=request.session['User'])),
			"all_users": User.objects.all(),
			"all_messages": Message.objects.all(),
			"all_comments":Comment.objects.all(),
			}
		return render(request, 'messageboard.html', context)
	else: 
		print('user must be logged in')
		return redirect('/register')	

def create_message(request):
	context = {
		"logged_User": User.objects.get(id=request.session['User']),
		"all_message": Message.objects.all(),
		"all_comments":Comment.objects.all(),
		}
	return render(request, 'create_message.html', context)

def post_message(request):
	Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['User']))
	return redirect('/messageboard')

def post_comment(request, user_id):
	user = User.objects.get(id=request.session['User'])
	message = Message.objects.get(id=request.POST['message'])

	Comment.objects.create(comment=request.POST['comment'], user=user, message=message)
	return redirect('/messageboard')

def delete_message(request, message_id):
	delete_message = Message.objects.get(id=message_id)
	delete_message.delete()
	return redirect('/messageboard')

def logout(request):
	request.session.clear()
	return redirect('/')

def quiz(request):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),	
		}
		return render(request, "quiz.html", context)
	else:
		return render(request, "quiz.html")

def trail_family(request):
	if 'User' in request.session:
		context = {
			"logged_User": User.objects.get(id=request.session['User']),	
		}
		return render(request, "trail_family.html", context)
	else:
		return render(request, 'trail_family.html')

def fam_results(request):
	states = request.POST['states']
	context = {
	"trail_family": Trailfam.objects.filter(state = states),
	}
	
	return render( request, 'trail_family.html', context)
									
