from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_page, name="about_page"),
    path("resources/", views.resource_list, name="resource_list"),
    path("resources/<int:resource_id>/", views.resource_detail, name="resource_detail"),
    path('feedback/', views.feedback, name='feedback'),
    path('upload/', views.upload_solution, name='upload_solution'),
path('upload/success/', views.upload_success, name='upload_success'),
    path("chapters/", views.chapter_list, name="chapter_list"),  # New chapter list page
    path("chapter/<int:id>/", views.chapter_detail, name="chapter_detail"),
    path('section/<int:id>/', views.section_detail, name='section_detail'),
    path("chapter/<int:chapter_id>/section/<int:section_id>/", views.section_detail, name="section_detail"),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path("problem/<int:problem_id>/", views.problem_detail, name="problem_detail"),
    path("upload/<int:problem_id>/", views.upload_solution, name="upload_solution"),
    path("review/", views.review_solutions, name="review_solutions"),
    path("approve/<int:solution_id>/", views.approve_solution, name="approve_solution"),
    path("reject/<int:solution_id>/", views.reject_solution, name="reject_solution"),
]