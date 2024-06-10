from django.shortcuts import render

from category.forms import newcategory

# Create your views here.
def add_category(request):
    if request.method=='POST':
        form=newcategory(request.POST)
        form.is_valid()
        form.save()
    else:
        form=newcategory()

    return render(request,'category.html',{'form':form})