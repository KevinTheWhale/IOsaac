from django import forms
from .models import SolutionImage, Feedback, Chapter, Section, Problem

class UploadSolutionForm(forms.ModelForm): # For users to upload their solutions
    class Meta:
        model = SolutionImage
        fields = ['problem', 'image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type in ['image/png', 'image/jpeg']:
                raise forms.ValidationError("Only PNG or JPEG files are allowed.")
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File too large (max 5MB).")
        return image



class SolutionImageForm(forms.ModelForm):
    class Meta:
        model = SolutionImage
        fields = ['image']
    
    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Restrict file size (max 5MB)
        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Image file too large (max 5MB).")

        # Allow only PNG and JPG formats
        allowed_extensions = ['png', 'jpg', 'jpeg']
        if not image.name.lower().endswith(tuple(allowed_extensions)):
            raise forms.ValidationError("Only PNG and JPG images are allowed.")

        return image

class FeedbackForm(forms.ModelForm): # For User Feedback
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80})
        }