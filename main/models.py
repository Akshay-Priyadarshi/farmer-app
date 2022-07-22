from django.db import models
import uuid

class Crop(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()

class Fertilizer(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  name = models.TextField()
  price_per_unit = models.FloatField()
  quantity_unit = models.TextField()


class Farmer(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  name = models.TextField()
  phone_number = models.CharField(max_length=15)
  language = models.TextField()

class Farm(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  area = models.TextField()
  village = models.TextField()
  farmer = models.ForeignKey(Farmer,on_delete=models.RESTRICT)
  crop = models.ForeignKey(Crop,on_delete=models.RESTRICT)
  sowing_date = models.DateField()


class Schedule(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  farm = models.ForeignKey(Farm,on_delete=models.RESTRICT)
  fertilizer = models.OneToOneField(Fertilizer,on_delete=models.RESTRICT)
  quantity = models.FloatField()

