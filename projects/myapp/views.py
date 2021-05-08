from django.shortcuts import render, redirect
from myapp.models import Project

# Create your views here.


def ProjectDetail(requset):
	project = Project.objects.all()
	return render(requset, 'myapp/project.html', {'project':project})

def Description(requset, id):
	desc = Project.objects.get(id=id)
	return render(requset, 'myapp/description.html', {'desc':desc})

def ProjectAdd(requset):
	if requset.method == "POST":
		title = requset.POST.get('title')
		image = requset.FILES['image']
		description = requset.POST.get('description')
		technology_used = requset.POST.get('technology_used')
		project = Project(title=title, image=image, description=description, technology_used=technology_used)
		project.save()
		return redirect(ProjectDetail)
	return render(requset, 'myapp/projectadd.html')

