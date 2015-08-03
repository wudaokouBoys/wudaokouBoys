# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CBulletscreen(models.Model):
    id = models.IntegerField(db_column='BId', primary_key=True)  # Field name made lowercase.
    video = models.IntegerField(db_column='BVideo', blank=True, null=True)  # Field name made lowercase.
    time = models.FloatField(db_column='BTime', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='BContent', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulletscreen'


class CComment(models.Model):
    id = models.IntegerField(db_column='CId', primary_key=True)  # Field name made lowercase.
    upper = models.IntegerField(db_column='CUpper', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='CTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CContent', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    video = models.IntegerField(db_column='CVideo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class CType(models.Model):
    id = models.IntegerField(db_column='TId', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='TContent', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'


class CUser(models.Model):
    id = models.IntegerField(db_column='UId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='UName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='UPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='UEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='UImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    likenum = models.IntegerField(db_column='ULikenum', blank=True, null=True)  # Field name made lowercase.
    uphistory = models.CharField(db_column='UUphistory', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    viewhistory = models.CharField(db_column='UViewhistory', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    follow = models.CharField(db_column='UFollow', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    followme = models.CharField(db_column='UFollowme', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    admin = models.IntegerField(db_column='UAdmin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class CVideo(models.Model):
    id = models.IntegerField(db_column='VId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='VTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discribe = models.CharField(db_column='VDiscribe', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='VKeyword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='VType', blank=True, null=True)  # Field name made lowercase.
    upper = models.IntegerField(db_column='VUpper', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='VTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='VPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='VState', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='VComments', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    bsreen = models.CharField(db_column='VBsreen', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    likenum = models.IntegerField(db_column='VLikenum', blank=True, null=True)  # Field name made lowercase.
    playnum = models.IntegerField(db_column='VPlaynum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video'
