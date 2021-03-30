from django.shortcuts import render
from django.views import View
from .models import SideBarMenus, TeacherProfiles
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def teachers_side_bar_menus(request):
	context = dict()
	context['SideBarMenus'] = SideBarMenus.objects.filter(
		role=2
		).order_by('sortorder').all()[:4]
	return context


class TeachaerDashboard(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		current_user = request.user
		self.context = teachers_side_bar_menus(request)
		self.context["techer_profile"] = TeacherProfiles.objects.get(
			user=current_user
		)
		self.context["phone"] =  TeacherProfiles.objects.get(
			user=current_user
		).user.phone
		self.context["email"] =  TeacherProfiles.objects.get(
			user=current_user
		).user.email
		self.context['current_user'] = current_user
		return render(
			request, 'teacher/dashboard.html', self.context
		)


class TeacherProfile(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		return render(
			request, "teacher/teacher_profile.html", self.context
		)


class TeacherSearchJob(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		return render(
			request, "teacher/teacher_search_job.html", self.context
		)


class TeachaerTrackJob(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		return render(
			request, "teacher/teacher_track_job.html", self.context
		)
