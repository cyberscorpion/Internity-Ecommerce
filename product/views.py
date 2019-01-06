from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document
from .forms import *
#def home(request):
#    return render(request, 'home.html')



#class DocumentCreateView(CreateView):
#    model = Document
#    fields = ['upload', ]
#    success_url = reverse_lazy('home')
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        documents = Document.objects.all()
#        context['documents'] = documents
#        return context

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f=form.save()
            return redirect('home')
    else:
        form = ProductForm()
    context = {
        'form' : form,
    }
#            print("no name entered #P-10")
    return render(request,'product/add_product.html',context)


def all_product(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'product/all_product.html',context)
