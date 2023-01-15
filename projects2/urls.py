from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conference-publications/', views.pub, name='conference-publications'),
    path('single-conference-publications/<str:pk>', views.spub, name='single-conference-publications'),
    path('single-journal-publications/<str:pk>', views.sjpub, name='single-journal-publications'),
    path('journal-publications/', views.jpub, name='journal-publications'),
    path('create-publication/', views.createPublications, name='create-publication'),
    path('create-journal/', views.createJournalPublications, name='create-journal'),
    path('post-publication/', views.postPublications, name='post-publication'),
    path('publishing-event/', views.publishingEvents, name='publishing-event'),
    path('requesting-publications/', views.requestingPublications, name='requesting-publications'),
    path('rating-publications/', views.ratingPublications, name='rating-publications'),
    path('published-submissions', views.submissions, name='published-submissions'),
]