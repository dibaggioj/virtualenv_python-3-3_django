from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import UploadPhotoForm
from photos.models import UploadPhoto


# Create your views here.
def upload_photo(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'photos/afterupload.html')
    else:
        form = UploadPhotoForm()
    return render(request, 'photos/upload.html', {'form': form})


def display_photo(request):
    image_names = [p.file.name for p in UploadPhoto.objects.all()]
    return render(request, 'photos/listfiles.html', {'names': image_names})