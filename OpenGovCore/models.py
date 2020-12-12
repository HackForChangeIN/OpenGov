from django.db import models
from django.core.exceptions import FieldDoesNotExist
from autoslug import AutoSlugField

PARTY_TYPE = (
    ('National Party', 'National Party'),
    ('State Party', 'State Party'),
    ('Regional Party', 'Regional Party')

)

SESSION_NAME = (
    ('Monsoon Session','Monsoon Session'),
    ('Budget Session','Budget Session'),
    ('Winter Session','Winter Session')
)

class States(models.Model):
    name = models.CharField(max_length=200)
    name_slug=AutoSlugField(populate_from='name',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"


class Parliamentary_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10,blank=True)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')
    name_slug=AutoSlugField(populate_from='name',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parliamentary_Constituency"
        verbose_name_plural = "Parliamentary_Constituencies"


class Assembly_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10,blank=True)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')
    name_slug=AutoSlugField(populate_from='name',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Assembly_Constituency"
        verbose_name_plural = "Assembly_Constituencies"


class Parties(models.Model):
    party_name = models.CharField(max_length=500, blank=True)
    acronym = models.CharField(max_length=50, blank=True)
    type = models.CharField(choices=PARTY_TYPE, max_length=100)
    symbol = models.ImageField(null=True, blank=True)
    founded = models.CharField(max_length=200, blank=True)
    founder_name = models.CharField(max_length=200, blank=True)
    president_name = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=500, blank=True)
    party_name_slug=AutoSlugField(populate_from='party_name',blank=True)

    def __str__(self):
        return self.party_name

    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"


class Central_Legislatures(models.Model):
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    name_slug=AutoSlugField(populate_from='name',blank=True)
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Central_Legislature"
        verbose_name_plural = "Central_Legislatures"


class State_Legislatures(models.Model):
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    state_id = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')
    name_slug=AutoSlugField(populate_from='name',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State_Legislature"
        verbose_name_plural = "State_Legislatures"


class Term(models.Model):
    term_name = models.CharField(max_length=100, blank=True)
    start_year = models.CharField(max_length=100, blank=True)
    end_year = models.CharField(max_length=100, blank=True)
    central_legislature_id = models.ForeignKey(
        Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures')

    def __str__(self):
        return self.term_name

    class Meta:
        verbose_name = "Term"
        verbose_name_plural = "Terms"


class Sittings(models.Model):
    sitting_name = models.CharField(max_length=100, blank=True)
    start_year = models.CharField(max_length=100, blank=True)
    end_year = models.CharField(max_length=100, blank=True)
    state_legislature_id = models.ForeignKey(
        State_Legislatures, on_delete=models.CASCADE, verbose_name='State_Legislatures')

    def __str__(self):
        return self.sitting_name

    class Meta:
        verbose_name = "Sitting"
        verbose_name_plural = "Sittings"


class Parliamentary_Sessions(models.Model):
    type = models.CharField(max_length=200, blank=True)
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    central_legislature_id = models.ForeignKey(
        Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures', blank=True, null=True)
    session_name = models.CharField(choices=SESSION_NAME, max_length=100,blank=True)
    session_name_slug=AutoSlugField(populate_from='session_name',blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Parliamentary_Session"
        verbose_name_plural = "Parliamentary_Sessions"


class Assembly_Sessions(models.Model):
    type = models.CharField(max_length=200, blank=True)
    sitting_id = models.ForeignKey(
        Sittings, on_delete=models.CASCADE, verbose_name='Sittings', blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    state_legislature_id = models.ForeignKey(
        State_Legislatures, on_delete=models.CASCADE, verbose_name='State_Legislatures', blank=True, null=True)
    session_name = models.CharField(choices=SESSION_NAME, max_length=100,blank=True)
    session_name_slug=AutoSlugField(populate_from='session_name',blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Assembly_Session"
        verbose_name_plural = "Assembly_Sessions"


class Candidate(models.Model):
    name = models.CharField(max_length=500, blank=True)
    dob = models.CharField(max_length=200, blank=True)
    qualification = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    social_class = models.CharField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    profession = models.CharField(max_length=500, blank=True)
    criminal_cases = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True)
    present_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    source = models.URLField(max_length = 400,blank=True)
    total_assets = models.CharField(max_length=500, blank=True)
    total_liabilities = models.CharField(max_length=500, blank=True)
    name_slug=AutoSlugField(populate_from='name',blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"


class Candidature (models.Model):
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name='Candidate')
    party_id = models.ForeignKey(
        Parties, on_delete=models.CASCADE, verbose_name='Party', blank=True, null=True)
    state_id = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State', blank=True, null=True)
    type = models.CharField(max_length=200, blank=True)
    parliamentary_constituency_id = models.ForeignKey(Parliamentary_Constituencies, on_delete=models.CASCADE,
                                                      verbose_name='Parliamentary_Constituency', blank=True, null=True)
    assembly_constituency_id = models.ForeignKey(Assembly_Constituencies, on_delete=models.CASCADE,
                                                 verbose_name='Assembly_Constituency', blank=True, null=True)
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    sitting_id = models.ForeignKey(
        Sittings, on_delete=models.CASCADE, verbose_name='Sittings', blank=True, null=True)
    central_legislature_id = models.ForeignKey(
        Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures', blank=True, null=True)
    state_legislature_id = models.ForeignKey(
        State_Legislatures, on_delete=models.CASCADE, verbose_name='State_Legislatures', blank=True, null=True)

    """def __str__(self):
        return self.candidate_id"""

    class Meta:
        verbose_name = "Candidature"
        verbose_name_plural = "Candidatures"


class Questions(models.Model):
    title = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    type = models.CharField(max_length=200, blank=True)
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name='Asked by', blank=True, null=True)
    category = models.CharField(max_length=500, blank=True)
    date = models.DateField(blank=True)
    subject = models.CharField(max_length=500, blank=True)
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    sitting_id = models.ForeignKey(
        Sittings, on_delete=models.CASCADE, verbose_name='Sittings', blank=True, null=True)
    parliamentary_session_id = models.ForeignKey(Parliamentary_Sessions, on_delete=models.CASCADE,
                                                 verbose_name='Parliamentary_Sessions', blank=True, null=True)
    assembly_session_id = models.ForeignKey(Assembly_Sessions, on_delete=models.CASCADE,
                                            verbose_name='Assembly_Sessions', blank=True, null=True)
    central_legislature_id = models.ForeignKey(
        Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures', blank=True, null=True)
    state_legislature_id = models.ForeignKey(
        State_Legislatures, on_delete=models.CASCADE, verbose_name='State_Legislatures', blank=True, null=True)
    source = models.CharField(max_length=1000, blank=True)
    category_slug=AutoSlugField(populate_from='category',blank=True)
    subject_slug=AutoSlugField(populate_from='subject',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Debates(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    type = models.CharField(max_length=300, blank=True)
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name='Participants', blank=True, null=True)
    central_legislature_id = models.ForeignKey(
        Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures', blank=True, null=True)
    session_id = models.ForeignKey(Parliamentary_Sessions, on_delete=models.CASCADE,
                                                 verbose_name='Parliamentary_Sessions', blank=True, null=True)
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    date = models.DateField(blank=True)
    source = models.URLField(max_length = 400,blank=True)
    type_slug=AutoSlugField(populate_from='type',blank=True)
    title_slug=AutoSlugField(populate_from='title',blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Debate"
        verbose_name_plural = "Debates"

class Bills(models.Model):
    title = models.TextField(blank=True)
    type = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=200, blank=True)
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name='Introducer', blank=True, null=True)
    ministry = models.CharField(max_length=300, blank=True)
    date_of_introduction = models.DateField(blank=True)
    category = models.CharField(max_length=200, blank=True) 
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    sitting_id = models.ForeignKey(
        Sittings, on_delete=models.CASCADE, verbose_name='Sittings', blank=True, null=True)
    parliamentary_session_id = models.ForeignKey(Parliamentary_Sessions, on_delete=models.CASCADE,verbose_name='Parliamentary_Sessions', blank=True, null=True)
    assembly_session_id = models.ForeignKey(Assembly_Sessions, on_delete=models.CASCADE,verbose_name='Assembly_Sessions', blank=True, null=True)
    central_legislature_id =  models.ForeignKey(Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures', blank=True, null=True)
    state_legislature_id = models.ForeignKey(State_Legislatures, on_delete=models.CASCADE, verbose_name='State_Legislatures', blank=True, null=True) 
    source = models.URLField(max_length = 400,blank=True)
    debate_loksabha_date = models.CharField(max_length=200, blank=True)
    debate_rajyasabha_date = models.CharField(max_length=200, blank=True)
    title_slug=AutoSlugField(populate_from='title',blank=True)
    type_slug=AutoSlugField(populate_from='type',blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Bill"
        verbose_name_plural = "Bills"

class Attendance(models.Model):
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name='Member Name', blank=True, null=True)
    term_id = models.ForeignKey(
        Term, on_delete=models.CASCADE, verbose_name='Term', blank=True, null=True)
    session_id = models.ForeignKey(Parliamentary_Sessions, on_delete=models.CASCADE,verbose_name='Parliamentary_Sessions', blank=True, null=True)
    attendance_signed_days = models.CharField(max_length=200, blank=True)
    attendance_not_signed_days = models.CharField(max_length=200, blank=True)
    source = models.URLField(max_length = 400,blank=True)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance"
                                                
    
    

    
