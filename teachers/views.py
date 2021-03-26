from django.shortcuts import render
from django.views import View
from .models import SideBarMenus, TeacherProfiles
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class TeachaerDashboard(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		current_user = request.user
		self.context['SideBarMenus'] = SideBarMenus.objects.filter(role=2).order_by('sortorder').all()[:4]
		self.context["techer_profile"] = TeacherProfiles.objects.get(user=current_user)
		self.context["phone"] =  TeacherProfiles.objects.get(user=current_user).user.phone
		self.context["email"] =  TeacherProfiles.objects.get(user=current_user).user.email
		self.context['current_user'] = current_user
		return render(request, 'teacher/dashboard.html', self.context)