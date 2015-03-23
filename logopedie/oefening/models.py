from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Child(models.Model):
    userName = models.CharField(max_length=128,unique=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    age = models.IntegerField()
    picture = models.ImageField(upload_to='profile_pictures',null=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User,null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.userName)
        super(Child, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return u'%s %s' % (self.firstName, self.lastName)

class Opgave(models.Model):
    name = models.CharField(max_length=128,unique=True)
    question = models.CharField(max_length=256,default='Klik op het juiste antwoord', null=True)
    picture = models.ImageField(upload_to='Opgaves',null=True)
    optie1 = models.CharField(max_length=128, default='')
    optie2 = models.CharField(max_length=128, default='', null=True)
    optie3 = models.CharField(max_length=128, default='', null=True)
    optie4 = models.CharField(max_length=128, default='', null=True)
    correctAnswer = models.IntegerField(default=1)
    difficultyOptions = (
    	('0', 'Easy'),
        ('1', 'Medium'),
        ('2', 'Hard'),
    )
    categoryOptions = (
    	('1', 'Woordenschat'),
    	('2', 'Bijwoorden'),
        ('2', 'Ander')
    )
    category = models.CharField(max_length=2,choices=categoryOptions)
    
    difficulty = models.CharField(max_length=2,choices=difficultyOptions,default='1')
    slug = models.SlugField(unique=True,null=False)
    user = models.ForeignKey(User)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Opgave, self).save(*args, **kwargs)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class Oefeningenreeks(models.Model):
    name = models.CharField(max_length=128, unique=True)
    oefeningen = models.ManyToManyField(Opgave, null=True, blank=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Oefeningenreeks, self).save(*args, **kwargs)

class Answer(models.Model):
    child = models.ForeignKey('Child')
    opgave = models.ForeignKey('Opgave')
    answer = models.IntegerField(default=1)
    correctAnswer = models.IntegerField()
    correct = models.BooleanField(default=False)

class Resultaat(models.Model):
    child = models.ForeignKey('Child')
    oefeningenreeks = models.ForeignKey('Oefeningenreeks',default=None)
    date = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    answers = models.ManyToManyField(Answer, null=True, blank=True)
    ended = models.BooleanField(default=False)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    