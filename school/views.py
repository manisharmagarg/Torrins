from django.shortcuts import render
from django.views import View
from teachers.models import SideBarMenus
from .models import SchoolProfile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def school_side_bar_menus(request):
	context = dict()
	context['SideBarMenus'] = SideBarMenus.objects.filter(role=3).order_by('sortorder').all()[:6]
	return context


class SchoolDashboard(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		current_user = request.user
		self.context = school_side_bar_menus(request)
		self.context["school_profile"] = SchoolProfile.objects.get(
			user=current_user
		)
		self.context["phone"] =  SchoolProfile.objects.get(
			user=current_user
		).user.phone
		self.context["email"] =  SchoolProfile.objects.get(
			user=current_user
		).user.email
		self.context['current_user'] = current_user
		return render(
			request, 'school/dashboard.html', self.context
		)


class SchoolProfiles(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = school_side_bar_menus(request)
		return render(
			request, 'school/school_profile.html', self.context
		)


class SchoolPostJob(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = school_side_bar_menus(request)
		return render(
			request, 'school/school_post_job.html', self.context
		)


class SchoolBrowseTeacher(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = school_side_bar_menus(request)
		return render(
			request, 'school/school_browse_teacher.html', self.context
		)


class SchoolTrackJob(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = school_side_bar_menus(request)
		return render(
			request, 'school/school_track_job.html', self.context
		)


class SchoolMessage(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = school_side_bar_menus(request)
		return render(
			request, 'school/school_message.html', self.context
		)
