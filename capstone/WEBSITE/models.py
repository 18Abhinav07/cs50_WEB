from django.db import models

class INSTITUTE_ADMITTED(models.Model):
    
    created_at = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    reason =  models.CharField(max_length= 100)
    permission = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    batch = models.CharField(max_length=15)
    branch = models.CharField(max_length=10)
    vehicle_no = models.CharField(max_length=10)


class NON_INSTITUTE_ADMITTED(models.Model):
    
    created_at = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    reason=  models.CharField(max_length= 100)
    phone = models.CharField(max_length=10)
    vehicle_no = models.CharField(max_length=10)
    
    
class STUDENTS_DATA(models.Model):
    
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    room_no = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    batch = models.CharField(max_length=15)
    branch = models.CharField(max_length=10)
    
    
    

