from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conference, Journal, Faculty, Post
from .forms import ConferenceForm, JournalForm, PostForm, EventForm, RequestPublicationsForm, RatingForm


def home(request):
    return render(request, 'html-pages/home.html')

def pub(request):
    pub = Conference.objects.all()
    context = {'publications': pub}
    return render(request, 'html-pages/publications.html', context)

def jpub(request):
    jpub = Journal.objects.all()
    context = {'jpublications': jpub}
    return render(request, 'html-pages/Journal-publications.html', context)

def spub(request, pk):
    pubObj = Faculty.objects.all()
    context = {'pubObj': pubObj}
    return render(request, 'html-pages/single-publications.html', context)

def sjpub(request, pk):
    jpubObj = Faculty.objects.all()
    context = {'jpubObj': jpubObj}
    return render(request, 'html-pages/single-jpublications.html', context)

def submissions(request):
    subObj = Post.objects.all()
    context = {'subObj': subObj}
    return render(request, 'html-pages/published-submissions.html', context)

def createPublications(request):
    form = ConferenceForm()

    if request.method == "POST":
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference-publications')
    
    context = {'form': form}
    return render(request, "html-pages/html-forms.html", context)

def createJournalPublications(request):
    form  = JournalForm()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('journal-publications')

    context = {'form': form}
    return render(request, "html-pages/html-forms.html", context)

def postPublications(request):
    form = PostForm()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('published-submissions')

    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

def publishingEvents(request):
    form = EventForm()
    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

def requestingPublications(request):
    form = RequestPublicationsForm()
    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

def ratingPublications(request):
    form = RatingForm()
    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)