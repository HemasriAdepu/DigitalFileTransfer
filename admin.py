# members/admin.py
from django.contrib import admin
from .models import Member, Owner, File
from django.db import models
from django.contrib.auth.models import User

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'personal_question_1', 'personal_answer_1', 
                    'personal_question_2', 'personal_answer_2', 
                    'personal_question_3', 'personal_answer_3')
    search_fields = ('phone_number', 'personal_question_1', 'personal_answer_1', 
                     'personal_question_2', 'personal_answer_2', 
                     'personal_question_3', 'personal_answer_3')
    list_filter = ('phone_number',)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_by', 'upload_date')
    search_fields = ('file_name', 'uploaded_by')
    list_filter = ('uploaded_by',)
