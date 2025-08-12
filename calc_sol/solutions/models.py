from django.db import models
from django.contrib.auth.models import User


# Create your models here. 
# note: You need to migrate before redeploying!

class Chapter(models.Model): 
    number = models.IntegerField(unique=True)  # Example: 5
    title = models.CharField(max_length=255)  # Example: "Integrals"

    def __str__(self): # Return it to the frontend
        return f"Chapter {self.number}: {self.title}"

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="sections")
    number = models.CharField(max_length=10)  # Example: "1.1"
    title = models.CharField(max_length=255)  # Example: "Introduction to Limits"

    
    def __str__(self):
        return f"{self.chapter.number}.{self.number}: {self.title}"

class Problem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="problems")
    problem_number = models.CharField(max_length=50,blank=True,null=True)  # Example: "1"
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.section.chapter.number}.{self.section.number}: Problem {self.problem_number}"

class SolutionImage(models.Model):
    problem = models.ForeignKey(Problem, related_name='solution_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='solution_images/')
    description = models.TextField(blank=True, null=True)
    
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        # Navigate through relationships to get the chapter and section
        section = self.problem.section
        chapter = section.chapter
        return f"{chapter.number}.{section.number}: Problem {self.problem.problem_number} - Status: {self.status}"
    

class Update(models.Model): # Enables news/updates from the admin panel
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class About(models.Model): # Enables 'About' page from admin panel
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class SupportResource(models.Model): # Support/Resources page
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='support_resources/')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Feedback(models.Model): # User feedback, notify them how many active words they have, also let them know that their feedback has been submitted!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.submitted_at}"