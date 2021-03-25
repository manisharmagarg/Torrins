from django.db import models
from utils.base_models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class SchoolProfile(BaseModel):
	school_name = models.CharField(
		max_length=254, null=True, 
		blank=True, unique=True
	)
	school_email = models.EmailField(
		max_length=254, null=True, 
		blank=True,  unique=True
	)
	school_url = models.URLField(
		max_length=200, null=True, blank=True
	)
	_type = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	education_board = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	established_year = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	Profile_image = models.ImageField(upload_to ='static/uploads/')
	recruiter_name = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	recruiter_designation = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	recruiter_mobile_no = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	recruiter_email = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	principle_name = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	chairman_name = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	about = models.CharField(
		max_length=254, null=True, 
		blank=True
	)

	active = models.CharField(
		max_length=254, null=True, 
		blank=True
	)
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )

	class Meta:
		db_table = "school"
