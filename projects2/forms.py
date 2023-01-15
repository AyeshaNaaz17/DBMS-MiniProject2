from django.forms import ModelForm
from .models import Conference, Journal, Post, Event, RequestPublications, Rating
from django import forms

class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ['conferenceID', 'conferenceName', 'conferenceDOI', 'conferenceArticle', 'UGCListed', 'conferenceNationality']


class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['journalID', 'journalName', 'journalISSN', 'journalArticle', 'UGCListed', 'journalNationality']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['eventName', 'eventID', 'eventLocation']

class RequestPublicationsForm(ModelForm):
    class Meta:
        model = RequestPublications;
        fields = ['requestFrom', 'requestTo', 'accept']

class RatingForm(ModelForm):
    class Meta:
        model = Rating;
        fields = ['ratingID', 'ratingName', 'ratingComments', 'ratingStars']