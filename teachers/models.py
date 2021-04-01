from django.db import models
from utils.base_models import BaseModel
from django.contrib.auth import get_user_model
from accounts.models import Role

User = get_user_model()


# Create your models here.
class TeacherProfiles(BaseModel):
	first_name = models.CharField(
		max_length=254, null=True, blank=True
	)
	last_name = models.CharField(
		max_length=254, null=True, blank=True
	)
	DOB = models.CharField(
		max_length=254, null=True, blank=True
	)
	gender = models.BigIntegerField(
		null=True, blank=True
	)
	position = models.BigIntegerField(
		null=True, blank=True
	)
	experience_years = models.CharField(
		max_length=255, null=True, blank=True
	)
	marital_status = models.BigIntegerField(
		null=True, blank=True
	)
	children = models.BigIntegerField(
		null=True, blank=True
	)
	about = models.TextField(
		null=True, blank=True
	)
	profile_image = models.BigIntegerField(
		null=True, blank=True
	)
	video = models.BigIntegerField(
		null=True, blank=True
	)
	certificates = models.BigIntegerField(
		null=True, blank=True
	)
	id_proofs = models.BigIntegerField(
		null=True, blank=True
	)
	last_salary = models.DecimalField(max_digits=14, decimal_places=2, 
		null=True, blank=True
	)
	expected_salary = models.DecimalField(max_digits=14, decimal_places=2, 
		null=True, blank=True
	)
	opportunties = models.CharField(
		max_length=255, null=True, blank=True
	)
	full_time = models.IntegerField(
		null=True, blank=True
	)
	publish = models.IntegerField(
		null=True, blank=True
	)
	notice_period = models.IntegerField(
		null=True, blank=True
	)
	relocate_location = models.TextField(
		null=True, blank=True
	)
	primary_subject = models.BigIntegerField(
		null=True, blank=True
	)
	standards_taught = models.TextField(
		null=True, blank=True
	)
	secondary_subject = models.TextField(
		null=True, blank=True
	)
	activities = models.TextField(
		null=True, blank=True
	)
	ctet = models.IntegerField(
		null=True, blank=True
	)
	ctet_paper = models.CharField(
		max_length=255, null=True, blank=True
	)
	net = models.IntegerField(
		null=True, blank=True
	)
	professional_training = models.IntegerField(
		null=True, blank=True
	)
	examiner = models.IntegerField(
		null=True, blank=True
	)
	conducted_by = models.CharField(
		max_length=255, null=True, blank=True
	)
	training_days = models.IntegerField(
		null=True, blank=True
	)
	monthly_passed = models.CharField(
		max_length=255, null=True, blank=True
	)
	year_passed = models.CharField(
		max_length=255, null=True, blank=True
	)
	school_board = models.BigIntegerField(
		null=True, blank=True
	)
	duration = models.CharField(
		max_length=255, null=True, blank=True
	)
	latest_year = models.CharField(
		max_length=255, null=True, blank=True
	)
	comment = models.TextField(
		null=True, blank=True
	)
	completed_step = models.IntegerField(
		null=True, blank=True
	)
	completed_status = models.IntegerField(
		null=True, blank=True
	)

	active = models.IntegerField(
		null=True, blank=True
	)
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )

	class Meta:
		db_table = 'teacher'



class SideBarMenus(BaseModel):
	menu = models.CharField(max_length=255, null=True, blank=True)
	slug = models.CharField(max_length=255, null=True, blank=True)
	sortorder = models.IntegerField(null=True, blank=True)
	parent = models.BigIntegerField(null=True, blank=True)
	role = models.IntegerField(null=True, blank=True)
	icon = models.CharField(max_length=255, null=True, blank=True)
	active = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table = 'sidebar_menus'


class GlobalCodes(BaseModel):
	category = models.CharField(
		max_length = 255, null=True, blank=True
	)
	code = models.CharField(
		max_length=255, null=True, blank=True
	)
	description = models.TextField(
		null=True, blank=True
	)
	active = models.IntegerField(
		null=True, blank=True
	)

	class Meta:
		db_table = 'global_codes'


class Country(models.Model):
	sortname = models.CharField(
		max_length=255, null=True, blank=True
	)
	name = models.CharField(
		max_length=255, null=True, blank=True
	)
	phonecode = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table = 'countries'


class State(models.Model):
	name=models.CharField(
		max_length=100, null=True, blank=True
	)
	country_id = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table = 'state'


class Districts(models.Model):
	name= models.CharField(
		max_length=50, null=True, blank=True
	)
	state_id = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table = 'districts'