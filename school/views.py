from django.shortcuts import render
from django.views import View
from teachers.models import SideBarMenus
from .models import SchoolProfile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class SchoolDashboard(LoginRequiredMixin, View):
	context = dict()
	def get(self, request, *args, **kwargs):
		current_user = request.user
		# print(">>>>>>>>>>>>>>>>", user)
		self.context['SideBarMenus'] = SideBarMenus.objects.filter(role=3).order_by('sortorder').all()[:6]
		self.context["school_profile"] = SchoolProfile.objects.get(user=current_user)
		self.context["phone"] =  SchoolProfile.objects.get(user=current_user).user.phone
		self.context["email"] =  SchoolProfile.objects.get(user=current_user).user.email
		self.context['current_user'] = current_user
		ram = SchoolProfile.objects.get(user=current_user).updated_at

		print(">>>>>>>>>>>>.", SchoolProfile.objects.get(user=current_user).school_name)





		role = kwargs.get('role')
		print("role>>>>>>>>>>>>>", args)
		self.context['SideBarMenus'] = SideBarMenus.objects.filter(role=3).order_by('sortorder').all()[:6]

		return render(request, 'school/dashboard.html', self.context)