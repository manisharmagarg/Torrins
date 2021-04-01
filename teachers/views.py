from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse, QueryDict
from .models import SideBarMenus, TeacherProfiles, \
	GlobalCodes, Country, State, Districts

# Create your views here.


def teachers_side_bar_menus(request):
	"""
	Teacher Job Protal get all side bar menus details.
	"""
	context = dict()
	context['SideBarMenus'] = SideBarMenus.objects.filter(
		role=2
		).order_by('sortorder').all()[:4]
	return context


class TeachaerDashboard(LoginRequiredMixin, View):
	"""
	Teacher Job portal detail view
	"""
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
	"""
	Teacher Pofile details view
	"""
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		self.context["profile"] = TeacherProfiles.objects.get(
			user=request.user.id
		)
		self.context["Gender"] = GlobalCodes.objects.filter(
			category="gender"
		)
		self.context["Positions"] = GlobalCodes.objects.filter(
			category="Positions"
		)
		self.context["Marital_Status"] = GlobalCodes.objects.filter(
			category="MaritalStatus"
		)
		self.context["Subjects"] = GlobalCodes.objects.filter(
			category="subject"
		)
		self.context["Country"] = Country.objects.all()
		self.context["States"] = State.objects.filter(country_id=101)
		return render(
			request, "teacher/teacher_profile.html", self.context
		)


class TeacherSearchJob(LoginRequiredMixin, View):
	"""
	Teacher search job view
	"""
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		return render(
			request, "teacher/teacher_search_job.html", self.context
		)


class TeachaerTrackJob(LoginRequiredMixin, View):
	"""
	Techer Tracking job View
	"""
	context = dict()
	def get(self, request, *args, **kwargs):
		self.context = teachers_side_bar_menus(request)
		return render(
			request, "teacher/teacher_track_job.html", self.context
		)


class GetDistrict(View):
	"""
	Teacher Profile get all districts list
	"""
	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			state_id = request.POST.get('state_id')
			distt = Districts.objects.filter(state_id=state_id).values()
			return JsonResponse(
				{"district": list(distt)}
			)

class TeacherProfileUpdate(View):
	"""
	Teacher Profile update record
	"""
	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			teacher_id = request.POST.get("teacher_id")
			first_name = request.POST.get("first_name")
			last_name = request.POST.get("last_name")
			date_of_birth = request.POST.get("date_of_birth")
			gender = request.POST.get("gender")
			position = request.POST.get("position")
			total_experience = request.POST.get("total_experience")
			marital_status = request.POST.get("marital_status")
			children = request.POST.get("children")
			phone = request.POST.get("phone")
			whatsapp_phone = request.POST.get("whatsapp_phone")
			email = request.POST.get("email")
			address = request.POST.get("address")
			country = request.POST.get("country")
			state = request.POST.get("state")
			city_distt = request.POST.get("city_distt")
			Pincode = request.POST.get("Pincode")

			teacher_obj = TeacherProfiles.objects.get(id=teacher_id)
			teacher_obj.first_name = first_name
			teacher_obj.last_name = last_name
			teacher_obj.DOB = date_of_birth
			teacher_obj.gender = gender
			teacher_obj.position = position
			teacher_obj.experience_years = total_experience
			teacher_obj.marital_status = marital_status
			teacher_obj.children = children
			# teacher_obj.about
			# teacher_obj.profile_image
			# teacher_obj.video
			# teacher_obj.certificates
			# teacher_obj.id_proofs
			# teacher_obj.last_salary
			# teacher_obj.expected_salary
			# teacher_obj.opportunties
			# teacher_obj.full_time
			# teacher_obj.publish
			# teacher_obj.notice_period
			# teacher_obj.relocate_location
			# teacher_obj.primary_subject
			# teacher_obj.standards_taught
			# teacher_obj.secondary_subject
			# teacher_obj.activities
			# teacher_obj.ctet
			# teacher_obj.ctet_paper
			# teacher_obj.net
			# teacher_obj.professional_training
			# teacher_obj.examiner
			# teacher_obj.conducted_by
			# teacher_obj.training_days
			# teacher_obj.monthly_passed
			# teacher_obj.year_passed
			# teacher_obj.school_board
			# teacher_obj.duration
			# teacher_obj.latest_year
			# teacher_obj.comment
			# teacher_obj.completed_step
			# teacher_obj.completed_status
			teacher_obj.save()
			response = {
				"message": "Data saved Successfully",
				"status_code": 200
			}
			return JsonResponse(
				response, safe=False
			)