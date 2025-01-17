# Generated by Django 3.1.7 on 2021-03-25 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('school_name', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('school_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('school_url', models.URLField(blank=True, null=True)),
                ('_type', models.CharField(blank=True, max_length=254, null=True)),
                ('education_board', models.CharField(blank=True, max_length=254, null=True)),
                ('established_year', models.CharField(blank=True, max_length=254, null=True)),
                ('Profile_image', models.ImageField(upload_to='static/uploads/')),
                ('recruiter_name', models.CharField(blank=True, max_length=254, null=True)),
                ('recruiter_designation', models.CharField(blank=True, max_length=254, null=True)),
                ('recruiter_mobile_no', models.CharField(blank=True, max_length=254, null=True)),
                ('recruiter_email', models.CharField(blank=True, max_length=254, null=True)),
                ('principle_name', models.CharField(blank=True, max_length=254, null=True)),
                ('chairman_name', models.CharField(blank=True, max_length=254, null=True)),
                ('about', models.CharField(blank=True, max_length=254, null=True)),
                ('active', models.CharField(blank=True, max_length=254, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_schoolprofile_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_schoolprofile_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_schoolprofile_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'school',
            },
        ),
    ]
