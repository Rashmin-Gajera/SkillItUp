from datetime import datetime

from django.db import models
from mainapp.models import User
# Create your models here.


# Domain Model
class Domain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# SubDomain Model
class SubDomain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Topic Model
class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    subdomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Educational Institutes
class EducationalInstitute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    subdomains = models.ManyToManyField(SubDomain, blank=True)
    students = models.ManyToManyField(User, blank=True)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Event Model
class Event(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    place = models.CharField(max_length=100)
    date = models.DateField()
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


# TrendingTech
class TrendingTech(models.Model):
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    companies = models.TextField()
    popularity = models.FloatField()
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# TrendingTools
class TrendingTool(models.Model):
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    popularity = models.FloatField()
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Profession
class Profession(models.Model):
    role = models.CharField(max_length=100)
    description = models.TextField()
    responsibilites = models.TextField()
    expected_salary = models.IntegerField()
    technologies = models.ManyToManyField(TrendingTech, blank=True)
    tools = models.ManyToManyField(TrendingTool, blank=True)
    img = models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.role


# Course Model
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    certificate = models.BooleanField(default=False)
    url = models.TextField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(TrendingTech, blank=True)
    tools = models.ManyToManyField(TrendingTool, blank=True)
    professions = models.ManyToManyField(Profession)

    def __str__(self):
        return self.name


# Reccomendation Test
class RecommendationTest(models.Model):
    LEARNER = 0
    INTERMEDIATE = 1
    PROFICIENT = 2
    EXPERT = 3
    GRADE_CHOICES = (
        (LEARNER, 'Learner'),
        (INTERMEDIATE, 'Intermediate'),
        (PROFICIENT, 'Proficient'),
        (EXPERT, 'Expert')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    certificate = models.CharField(max_length=200)
    data_structure = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    operating_system = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    database_management = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    computer_networks = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    cryptography = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    object_oriented_programming = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    computer_graphics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    digital_electronics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    engineering_mathematics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    statistics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    communication = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    english = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    programming = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    creativity = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    hackathon = models.BooleanField(default=False)
    hackathon_role = models.BooleanField(default=False)
    creative_critical = models.BooleanField(default=False)
    self_learning = models.BooleanField(default=False)
    management_technical = models.BooleanField(default=False)
    gaming = models.BooleanField(default=False)
    art = models.BooleanField(default=False)
    literature = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.profession.role


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Expert Model
class Expert(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic, blank=True)
    technologies = models.ManyToManyField(TrendingTech, blank=True)
    tools = models.ManyToManyField(TrendingTool, blank=True)
    available = models.BooleanField(default=False, blank=True)
    description = models.TextField()
    languages = models.ManyToManyField(Language)
    years = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name

