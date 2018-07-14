from django.shortcuts import render, render_to_response
from studentapp.models import Student
from studentapp.forms import StudentForm
from django.views import View
from django.shortcuts import redirect

# Create your views here.

class Home(View):

    def get(self, request):
        sform = StudentForm()
        data = Student.objects.all()
        return render(request, 'home.html', {'form':sform, 'data': data})

    def post(self, request):
        sdata = StudentForm(self.request.POST,self.request.FILES)
        if sdata.is_valid():
            sdata.save()
            return redirect('/')
        else:
            errors = sdata.errors
            return render(request, 'home.html', {'form': errors})

    def delete(self, request):
        id = self.request.GET.get('id')
        dels = Student.objects.get(id=id)
        dels.delete()
        data = Student.objects.all()
        return render(request, 'home.html', {'data': data})