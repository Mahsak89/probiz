from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Business Strategy Development", "Business Strategy Development"),
    ("Financial Planning and Analysis", "Financial Planning and Analysis"),
    ("Market Research and Analysis", "Market Research and Analysis"),
    ("Process Optimization", "Process Optimization"),
    ("Leadership Development", "Leadership Development"),
    ("Change Management", "Change Management"),
    ("consulting", "consulting"),
)
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)
