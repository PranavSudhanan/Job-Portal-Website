from django.db import models

# Create your models here.

class regmodel(models.Model):
    companyname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    number = models.IntegerField()
    address = models.CharField(max_length=100)

class upmodel(models.Model):
    cname = models.CharField(max_length=50)
    email = models.EmailField()
    jtitle = models.CharField(max_length=25)
    jtype = models.CharField(max_length=25)
    wtype = models.CharField(max_length=25)
    exp = models.CharField(max_length=25)
    qualify = models.CharField(max_length=70)

class addmodel(models.Model):
    catchoice = [
        ('Part-Time','Part-Time'),
        ('Full-Time','Full-Time'),

    ]
    cho=[
        ('Hybrid','Hybrid'),
        ('Remote','Remote'),
    ]
    choice=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]

    cname = models.CharField(max_length=50)
    email = models.EmailField()
    jtitle = models.CharField(max_length=25)
    jtype = models.CharField(max_length=25,choices=catchoice)
    wtype = models.CharField(max_length=25,choices=cho)
    exp = models.CharField(max_length=25,choices=choice)
    qualify = models.CharField(max_length=70)

class userprofilemodel(models.Model):
    uid=models.IntegerField()
    image = models.ImageField(upload_to='capp/static')
    fname = models.CharField(max_length=25)
    email = models.EmailField()
    resume = models.FileField(upload_to='capp/static')
    qualify = models.CharField(max_length=70)
    exp = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

class jobapplymodel(models.Model):
    cname = models.CharField(max_length=50)
    jtitle = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    resume = models.FileField(upload_to='capp/static')

class wishlistmodel(models.Model):
    cname = models.CharField(max_length=50)
    email = models.EmailField()
    jtitle = models.CharField(max_length=25)
    jtype = models.CharField(max_length=25)
    wtype = models.CharField(max_length=25)
    exp = models.CharField(max_length=25)
    qualify = models.CharField(max_length=70)

