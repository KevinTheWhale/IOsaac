from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Chapter, Section, Problem, SolutionImage, Update, About, SupportResource, Feedback
from .forms import SolutionImageForm, FeedbackForm, UploadSolutionForm
from django.utils import timezone



# Create your views here.

def home(request): # Home page
    chapters = Chapter.objects.all()
    updates = Update.objects.all().order_by('-created_at')  # Retrieve all updates, ordered by the most recent
    return render(request, "solutions/home.html", {"chapters": chapters, "updates": updates})

def about_page(request): # About page
    about = About.objects.last()  # Retrieve the most recent About content
    return render(request, "solutions/about.html", {"about": about})

def resource_list(request):
    resources = SupportResource.objects.all()
    return render(request, "solutions/resource_list.html", {"resources": resources})

def resource_detail(request, resource_id):
    resource = get_object_or_404(SupportResource, id=resource_id)
    return render(request, "solutions/resource_detail.html", {"resource": resource})

@login_required
def feedback(request):
    form = FeedbackForm()
    feedbacks_today = Feedback.objects.filter(user=request.user, submitted_at__date=timezone.now().date())
    
    if len(feedbacks_today) >= 3:
        return render(request, 'solutions/feedback.html', {'form': form, 'error': 'You have reached the daily feedback limit of 3.'})

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback')
    
    return render(request, 'solutions/feedback.html', {'form': form})

def chapter_detail(request, id): 
    chapter = get_object_or_404(Chapter, pk=id)  # Get the chapter with the given id
    return render(request, 'solutions/chapter_detail.html', {'chapter': chapter})

def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, "solutions/chapter_list.html", {"chapters": chapters})

def chapter_sections(request, chapter_id): # Chapter Page
    chapter = get_object_or_404(Chapter, id=chapter_id)
    sections = Section.objects.filter(chapter=chapter)  # Filter sections for this chapter
    return render(request, "solutions/chapter_sections.html", {"chapter": chapter, "sections": sections})

def section_detail(request, id):
    section = get_object_or_404(Section, pk=id)
    return render(request, 'solutions/section_detail.html', {'section': section})
'''
def problem_detail(request, id):
    # Get the specific problem by ID
    problem = get_object_or_404(Problem, id=id)
    
    # Retrieve associated solution images
    solution_images = problem.solution_images.all()  # Retrieve all associated solution images for the problem
    
    return render(request, 'solutions/problem_detail.html', {'problem': problem, 'solution_images': solution_images})
'''

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    solution_images = problem.solution_images.all().order_by('uploaded_at')
    return render(request, 'solutions/problem_detail.html', {
        'problem': problem,
        'solution_images': solution_images,
    })

@login_required
def upload_solution(request):
    if request.method == 'POST':
        form = UploadSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.uploaded_by = request.user
            solution.status = 'Pending'
            solution.save()
            return redirect('upload_success')
    else:
        form = UploadSolutionForm()
    
    return render(request, 'solutions/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'solutions/upload_success.html')

'''
@login_required
def upload_solution(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == "POST":
        form = SolutionImageForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.problem = problem
            solution.uploaded_by = request.user
            solution.status = "Pending"  # Moderation applies
            solution.save()
            return redirect("problem_detail", problem_id=problem.id)
    else:
        form = SolutionImageForm()

    return render(request, "solutions/upload_solution.html", {"form": form, "problem": problem})
'''

def is_admin(user):
    return user.is_staff  # Only admins can access moderation

@login_required
@user_passes_test(is_admin)
def review_solutions(request):
    pending_solutions = SolutionImage.objects.filter(status="Pending")
    return render(request, "solutions/review_solutions.html", {"pending_solutions": pending_solutions})

@login_required
@user_passes_test(is_admin)
def approve_solution(request, solution_id):
    solution = get_object_or_404(SolutionImage, id=solution_id)
    solution.status = "Approved"
    solution.save()
    return redirect("review_solutions")

@login_required
@user_passes_test(is_admin)
def reject_solution(request, solution_id):
    solution = get_object_or_404(SolutionImage, id=solution_id)
    solution.status = "Rejected"
    solution.save()
    return redirect("review_solutions")