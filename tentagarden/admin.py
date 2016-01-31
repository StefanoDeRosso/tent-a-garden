from django.contrib import admin
from .models import File, Post, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'website')
	search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
	readonly_fields = ('email', 'first_name', 'last_name')
	
	def username(self, obj):
		return obj.user.username
	def email(self, obj):
		return obj.user.email
	def first_name(self, obj):
		return obj.user.first_name
	def last_name(self, obj):
		return obj.user.last_name

admin.site.register(File)
admin.site.register(Post)
admin.site.register(UserProfile, UserProfileAdmin)
