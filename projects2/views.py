from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conference, Journal, Faculty, Post, Event, RequestPublications, Rating
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
    submissions = Post.objects.all()
    context = {'submissions': submissions}
    return render(request, 'html-pages/published-submissions.html', context)

def EventSubmissions(request):
    eveObj = Event.objects.all()
    context = {'eveObj': eveObj}
    return render(request, 'html-pages/published-events.html', context)

def requestingPapers(request):
    reqObj = RequestPublications.objects.all()
    context = {'reqobj': reqObj}
    return render(request, 'html-pages/profile-home.html', context)

def ratedPublications(request):
    r = Rating.objects.all()
    context = {'r': r}
    return render(request, 'html-pages/ratedPublications.html', context)

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

    if request.method == "POST":
        if form.is_valid():
            if form.save():
                return redirect('published-events')

    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

def requestingPublications(request):
    form = RequestPublicationsForm()

    if request.method == "POST":
        if form.is_valid():
            if form.save():
                return redirect('profile-home')

    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

def ratingPublications(request):
    form = RatingForm()

    if request.method == "POST":
        if form.is_valid():
            if form.save():
                return redirect('ratedPublications')

    context = {'form': form}
    return render(request,  "html-pages/html-forms.html", context)

