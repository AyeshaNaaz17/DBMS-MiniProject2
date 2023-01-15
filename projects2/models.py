from django.db import models
import uuid

class Faculty(models.Model):
    roles = (
        ('HOD', 'HOD'),
        ('Other', 'Other')
    )

    gender = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    def age(self):
        import datetime
        dob = self.facultyAge
        tod = datetime.date.today()
        myAge = (tod.year - dob.year) - int((tod.month, tod.today) < (dob.month, dob.day))
        return myAge


    facultyID = models.CharField(max_length=20, primary_key=True)
    facultyName = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=roles)
    departmentName = models.CharField(max_length=20)
    facultyAge = models.DateField()
    requestToID = models.ManyToManyField('RequestPublications')
    facultyEmail = models.EmailField(max_length=254)
    facultyGender = models.CharField(max_length=10, choices=gender)
    facultyPhone = models.CharField(max_length=10, unique=True)
    accountPassword = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.facultyID} {self.facultyName}' 

    


class Conference(models.Model):
    listed = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    facultyName = models.CharField(max_length=30)
    facultyDept = models.CharField(max_length=20)
    facultyID = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    conferenceID = models.CharField(max_length=20, unique=True, primary_key=True)
    conferenceName = models.CharField(max_length=50)
    conferenceDOI = models.CharField(max_length=30)
    conferenceArticle = models.ImageField(null=True, blank=True)
    rating_total = models.IntegerField(default=0, null=True, blank=True)
    UGCListed = models.CharField(max_length=200, choices=listed)
    conferenceNationality = models.CharField(max_length=60)

    def __str__(self):
        return self.conferenceName

class Journal(models.Model):
    listed = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    facultyName = models.CharField(max_length=30)
    facultyDept = models.CharField(max_length=20)
    facultyID = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    journalID = models.CharField(max_length=20, unique=True, primary_key=True)
    journalName = models.CharField(max_length=50)
    journalISSN = models.CharField(max_length=10)
    journalArticle = models.ImageField(null=True, blank=True)
    UGCListed = models.CharField(max_length=20 ,choices=listed)
    journalNationality = models.CharField(max_length=60)

    def __str__(self):
        return self.journalName



class RequestPublications(models.Model):
    decision = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    requestFrom = models.CharField(max_length=50)
    accept = models.CharField(max_length=10, choices=decision)
    time = models.DateTimeField(auto_now_add=True)
    requestTo = models.CharField(max_length=50)
    # requestToID = models.ManyToManyField(Faculty)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


    def __str__(self):
        return self.requestFrom

class Event(models.Model):
    eventLocation = models.TextField(max_length=500)
    eventName = models.CharField(max_length=200)
    eventID = models.ManyToManyField(Faculty, max_length=30)
    eventDate = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.eventName


class Post(models.Model):
    category = (
        ('Conference', 'Conference'),
        ('Journal', 'Journal')
    )
    postTime = models.DateTimeField(auto_now_add=True)
    postID = models.ManyToManyField(Faculty, max_length=20)
    ratings = models.ManyToManyField('Rating', null=True, blank=True)
    postCategory = models.CharField(max_length=50, choices=category)
    postSnaps = models.ImageField(null=True, blank=True, default='default.jpg')
    postTags = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.postCategory


class Rating(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down Vote')
    )
    ratingID = models.ManyToManyField(Faculty)
    ratingName = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratingComments = models.TextField(max_length=300)
    ratingStars = models.CharField(max_length=10, choices=VOTE_TYPE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.ratingStars
