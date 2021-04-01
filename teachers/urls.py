"""
Script to Define the urls related to teachers
"""
# pylint: disable=import-error
# pylint: disable=invalid-name

from django.urls import path
from .views import (
    TeachaerDashboard,
    TeacherProfile,
    TeacherSearchJob,
    TeachaerTrackJob,
    GetDistrict,
    TeacherProfileUpdate,
)


urlpatterns = [
    path(
        'dashboard/',
        TeachaerDashboard.as_view(),
        name='teachaer_dashboard',
    ),
    path(
        'profile/',
        TeacherProfile.as_view(),
        name='teachaer_profile'
    ),
    path(
        'search_job/',
        TeacherSearchJob.as_view(),
        name='teacher_search_job'
    ),
    path(
        'track_job/',
        TeachaerTrackJob.as_view(),
        name='teacher_track_job'
    ),
    path("get_district/",
        GetDistrict.as_view(),
        name="get_district"
    ),
    path("profile/update/",
        TeacherProfileUpdate.as_view(),
        name="get_district"
    ),
]
