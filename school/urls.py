"""
Script to Define the urls related to school
"""
# pylint: disable=import-error
# pylint: disable=invalid-name

from django.urls import path
from .views import (
    SchoolDashboard,
    SchoolProfiles,
    SchoolPostJob,
    SchoolBrowseTeacher,
    SchoolTrackJob,
    SchoolMessage,
)


urlpatterns = [
    path(
        'dashboard/',
        SchoolDashboard.as_view(),
        name='school_dashboard',
    ),
    path(
        'profile/',
        SchoolProfiles.as_view(),
        name='school_profile',
    ),
    path(
        'post_job/',
        SchoolPostJob.as_view(),
        name='school_post_job',
    ),
    path(
        'browseteacher/',
        SchoolBrowseTeacher.as_view(),
        name='school_browse_teacher',
    ),
    path(
        'track_job/',
        SchoolTrackJob.as_view(),
        name='school_track_job',
    ),
    path(
        'message/',
        SchoolMessage.as_view(),
        name='school_message',
    ),
]
