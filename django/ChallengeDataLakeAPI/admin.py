from django.contrib import admin
from .models import AdzunaJob, Database, Platform, TopTech, WebFramework, UserAPIKey, GithubRepo,JobOffer, RemoteokJob

admin.site.register(AdzunaJob)
admin.site.register(Database)
admin.site.register(Platform)
admin.site.register(TopTech)
admin.site.register(WebFramework)
admin.site.register(UserAPIKey)
admin.site.register(GithubRepo)
admin.site.register(JobOffer)
admin.site.register(RemoteokJob)
