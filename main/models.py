from django.db import models
import uuid

class Crop(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()

  def __str__(self):
    return self.name

class Fertilizer(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  name = models.TextField()
  price_per_unit = models.FloatField()
  quantity_unit = models.TextField()
  def __str__(self):
    return self.name


class Farmer(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  name = models.TextField()
  phone_number = models.CharField(max_length=15)
  language = models.TextField()
  def __str__(self):
    return self.name

class Farm(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  area = models.TextField()
  village = models.TextField()
  farmer = models.ForeignKey(Farmer,on_delete=models.RESTRICT)
  crop = models.ForeignKey(Crop,on_delete=models.RESTRICT)
  sowing_date = models.DateField()
  def __str__(self):
    return self.id + " " + self.village + " " + self.crop.name


class Schedule(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  farm = models.ForeignKey(Farm,on_delete=models.RESTRICT)
  fertilizer = models.OneToOneField(Fertilizer,on_delete=models.RESTRICT)
  quantity = models.FloatField()
  def __str__(self):
    return f"{self.farm.id} {self.fertilizer.name} {self.quantity}"

