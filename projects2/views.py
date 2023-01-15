from django.shortcuts import render
from .models import Conference, Journal

publicationList = [            
            {
                'facultyID': '1',
                'facultyName': 'Alia',
                'conferenceName': 'Sleep',
                'confernceDescription': 'Sleep is important'
            },
            {
            'facultyID': '2',
            'facultyName': 'Angela',
            'conferenceName': 'WebDev',
            'conferenceDescription': 'WebDev is fun'
            },
            {
            'facultyID': '3',
            'facultyName': 'Elizabeth',
            'conferenceName': 'Maths',
            'conferenceDescription': 'Maths is needed for all'
            }
        ]


def home(request):
    return render(request, 'html-pages/home.html')

def pub(request):
    pub = Conference.objects.all()
    context = {'publication': pub}
    return render(request, 'html-pages/publications.html', context)

def spub(request, pk):
    pubObj = Conference.objects.get(conferenceID=pk)
    rating_total = pubObj.rating_total.all()
    context = {'pubObj': pubObj, 'rating_total': rating_total}
    return render(request, 'html-pages/single-publications.html', context)