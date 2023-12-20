from itertools import product
from django.contrib import admin
from .models import Testimonial, Employee,Profile,Project,Job
# Register your models here.
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Employee)
admin.site.register(Testimonial)
admin.site.site_header = "Sargasso Admin"
admin.site.site_title = "Sargasso Admin Portal"
admin.site.index_title = "Sargasso Reclamation Portal"
