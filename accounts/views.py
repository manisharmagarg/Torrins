from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from .models import User, Role
from teachers.models import TeacherProfiles

class SignUpView(View):
	context = dict()
	def get(self, request, *args, **kwargs):
		return render(request, 'register.html', self.context)

	def post(self, request, *args, **kwargs):
		role = request.POST.get("role")
		school_name = request.POST.get("school_name")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		password = request.POST.get("password")

		try:
			role_obj = Role.objects.get(name=role)
			if role == "teacher":
				user_obj = User()
				user_obj.first_name = first_name
				user_obj.last_name = last_name
				user_obj.email = email
				user_obj.phone = phone
				user_obj.set_password(password)
				user_obj.role_id = role_obj
				user_obj.save()

				# save teacher profile
				teacher_obj = TeacherProfiles()
				teacher_obj.first_name = first_name
				teacher_obj.last_name = last_name
				teacher_obj.user = user_obj
				teacher_obj.save()
			elif role == "school":
				user_obj = User()
				user_obj.first_name = first_name
				user_obj.last_name = last_name
				user_obj.email = email
				user_obj.phone = phone
				user_obj.set_password(password)
				user_obj.role_id = role_obj
				user_obj.save()

				# save school profile
				school_profile_obj = SchoolProfile()
				school_profile_obj.school_name = user_obj.first_name
				school_profile_obj.school_email = user_obj.email
				school_profile_obj.user = user_obj
				school_profile_obj.save()
			return redirect('login_view')
		except Exception as exp:
			return render(request, 'register.html', self.context)



class LoginView(View):
	context = dict()
	def get(self, request, *args, **kwargs):
		return render(request, "login.html", self.context)

	def post(self, request, *args, **kwargs):
		email = request.POST.get("email")
		password = request.POST.get("password")
		try:
			user = authenticate(request, email=email, password=password)
			return render(request, 'dashboard.html', self.context)
		except Exception as exp:
			return render(request, "login.html", self.context)