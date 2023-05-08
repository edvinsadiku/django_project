from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Postimet, Category,Document
from .forms import DocumentForm


class HomeView(ListView):
    model = Postimet
    template_name = 'index.html'
    ordering = ['-pub_date']


    def get_queryset(self):
        categories = Category.objects.filter(name__in=['lajmet', 'konkurset','projektet','prokurimi'])
        queryset = super().get_queryset()
        queryset = queryset.filter(category__in=categories)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lajmet_posts = self.get_queryset().filter(category__name='lajmet')[:3]
        konkurset_posts = self.get_queryset().filter(category__name='konkurset')[:3]
        projektet_posts = self.get_queryset().filter(category__name='projektet')[:3]
        prokurimi_posts = self.get_queryset().filter(category__name='prokurimi')[:3]
        context['lajmet_posts'] = lajmet_posts
        context['projektet_posts'] = projektet_posts
        context['prokurimi_posts'] = prokurimi_posts
        context['konkurset_posts'] = konkurset_posts
        return context


def CategoryView(request, cats):
    category = get_object_or_404(Category, name__iexact=cats)
    category_posts = Postimet.objects.filter(category=category)
    return render(request, 'lista.html', {'category': category, 'category_posts': category_posts})


class ListaView(ListView):
    model = Postimet
    template_name='home2.html'

class PostimetView(DetailView):
    model = Postimet
    template_name='lajmi_single.html'


class ContactView(TemplateView):
    model = Postimet
    template_name='contact.html'


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'qenavyn.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})



