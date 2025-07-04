from django.db import models
from django.contrib.auth.models import User
import secrets

class UserAPIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)

class AdzunaJob(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    skills = models.TextField()

    class Meta:
        db_table = 'adzuna_job'

class Database(models.Model):
    id = models.AutoField(primary_key=True)
    database = models.CharField(max_length=100)
    usage_count = models.IntegerField()

    class Meta:
        db_table = 'database'

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=100)
    usage_count = models.IntegerField()

    class Meta:
        db_table = 'platform'

class TopTech(models.Model):
    id = models.AutoField(primary_key=True)
    offer_count = models.IntegerField()
    technology = models.CharField(max_length=100)

    class Meta:
        db_table = 'top_tech'

class WebFramework(models.Model):
    id = models.AutoField(primary_key=True)
    web_framework = models.CharField(max_length=100)
    usage_count = models.IntegerField()

    class Meta:
        db_table = 'web_framework'

class GithubRepo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    stargazers_count = models.IntegerField()
    forks_count = models.IntegerField()
    html_url = models.CharField(max_length=500)
    open_issues_count = models.IntegerField()
    watchers_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    license = models.CharField(max_length=255)
    homepage = models.CharField(max_length=500)

    class Meta:
        db_table = 'github_repo'

class JobOffer(models.Model):
    id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    remote = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'job_offer'
    


class RemoteokJob(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    job_link = models.TextField()

    class Meta:
        db_table = 'remoteok_job'