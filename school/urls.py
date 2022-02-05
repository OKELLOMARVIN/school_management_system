from django.urls import include, path

urlpatterns = [
    path('schools/', include('school.sch.urls')),
    path('teachers/', include('school.teacher.urls')),
    path('subjects/', include('school.subject.urls')),
    path('departments/', include('school.department.urls')),
]
