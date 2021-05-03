from django.db import models
import re
from .models import *
import bcrypt
from .models import *

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		
		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name should be at least 2 characters."
		else: 
			FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]+$')
			if not FIRSTNAME_REGEX.match(postData['first_name']):
				errors['first_name'] = "First name must contain only letters."
		if len(postData['last_name']) < 2:
			errors['last_name'] = "Last name should be at least 2 characters."
		else:
			LASTNAME_REGEX = re.compile(r'^[a-zA-Z]+$')
			if not LASTNAME_REGEX.match(postData['last_name']):
				errors['last_name'] = "Last name must contain only letters."
		if len(postData['username']) == 0:
			errors['username']	= "Username must be provided."
		if len(postData['username']) < 5:
			errors['username'] = "Username name should be at least 5 characters."	
		else:
			USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
			if not USERNAME_REGEX.match(postData['username']):
				errors['username'] = "Username must only contain letters and numbers."
		username = self.filter(username=postData['username'])
		if username:
			errors['username'] = "Username already used."	
		if len(postData['email']) == 0:
			errors['email']	= "Email address required."
		else:
			EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
			if not EMAIL_REGEX.match(postData['email']):
				errors['email'] = "Invalid email address!"
		email = self.filter(email=postData['email'])
		if email:
			errors['email'] = "Email address already used."		
		if len(postData['password']) < 8:
			errors['password']	= "Password must be at least 8 characters."
		if postData['password'] != postData['confirmPassword']:
			errors['password'] = 'Passwords must match'
		return errors

	def login_validator(self, postData):
		errors = {}
		login_username = User.objects.filter(username=postData['login_username'])
		if len(login_username) > 0:
			if bcrypt.checkpw(postData['login_pass'].encode(),login_username[0].password.encode()):
				print("password matches")
			else:
				errors['login_username'] ='Password does not match'
		else:
			errors['login_username'] = 'User with that username does not exist'
		return errors 		

class User(models.Model):
	first_name= models.CharField(max_length=45)
	last_name= models.CharField(max_length=45)
	username=models.CharField(max_length=20)
	email= models.CharField(max_length=60)
	password=models.CharField(max_length=80)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now = True)
	# admin = models.BooleanField(default = False)
	objects = UserManager()

	# jonathan = Users.objects.get(id=5)
	# jonathan.admin = True
	# jonathan.save()
	# bio_uploaded = a list of details associated with a given user
 	# user_messages = a list of messages associated with a given user
	def __repr__(self):
		return f"<User: {self.first_name} ({self.id})>"


class Bio(models.Model):
	location = models.CharField(max_length=80)
	fav_hike = models.CharField(max_length=80)
	uploaded_by = models.ForeignKey(User, related_name="bio_uploaded", on_delete = models.CASCADE)
		#User who uploaded bio
	bucket_list = models.CharField(max_length=80)
	snack = models.CharField(max_length=80)
	hike_need = models.CharField(max_length=80)
	profile_pic = models.ImageField(upload_to='images/', default='profile1.png')

	def __repr__(self):
		return f"<Bio: {self.location} ({self.id})>"

class Message(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User, related_name='user_messages', on_delete = models.CASCADE)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now= True)
	# message_comment = a comment associated with a message

class Comment(models.Model):
	comment = models.TextField()
	user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
	message = models.ForeignKey(Message, related_name='message_comment', on_delete = models.CASCADE)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now = True)

class Trailfam(models.Model):
	name = models.CharField(max_length=80)
	location = models.CharField(max_length=80)
	state = models.CharField(max_length=80)
	website = models.CharField(max_length= 100)
	objects = models.Manager()

	def __repr__(self):
		return f"<Trailfam: {self.name} {self.location} ({self.id})>"		







 	

