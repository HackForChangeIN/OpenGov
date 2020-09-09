from django.db import models

PARTY_TYPE = (
    ('National Party', 'National Party'),
    ('State Party', 'State Party'),
    ('Regional Party','Regional Party')

)

# Create your models here.
class States(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"


class Parliamentary_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parliamentary_Constituency"
        verbose_name_plural = "Parliamentary_Constituencies"


class Assembly_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Assembly_Constituency"
        verbose_name_plural = "Assembly_Constituencies"

class Parties(models.Model):
    party_name = models.CharField(max_length=500,blank = True)
    acronym = models.CharField(max_length=50,blank = True)
    type = models.CharField(choices=PARTY_TYPE,max_length=100)
    symbol = models.ImageField( null=True, blank=True)
    founded = models.CharField(max_length=200,blank = True) 
    founder_name = models.CharField(max_length=200,blank = True)
    president_name = models.CharField(max_length=200,blank = True)
    website = models.CharField(max_length=500,blank = True) 
    def __str__(self):
        return self.party_name
    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"
    
"""class Candidate(models.Model):
    name = models.CharField(max_length=500,blank = True)
    dob = models.CharField(max_length=200,blank = True) 
    qualification = models.CharField(max_length=500,blank = True)
    gender = models.CharField(max_length=100,blank = True)
    social_class = models.CharField(max_length=500,blank = True)
    contact_number = models.CharField(max_length=500,blank = True)
    email = models.CharField(max_length=500,blank = True)
    profession = models.CharField(max_length=500,blank = True)
    criminal_cases = models.CharField(max_length=500,blank = True) 
    photo = models.ImageField( null=True, blank=True)
    present_address = models.TextField(blank=True) 
    permanent_address = models.TextField(blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

class Candidature (models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='Candidate')
    party_id = models.ForeignKey(Parties, on_delete=models.CASCADE, verbose_name='Party')
    state_id = models.ForeignKey(States, on_delete=models.CASCADE, verbose_name='State')
    type = models.CharField(max_length=200,blank = True)
    parliamentary_constituency_id = models.ForeignKey(Parliamentary_Constituencies, on_delete=models.CASCADE, 
                                    verbose_name='Parliamentary_Constituency',blank=True, null=True)
    assembly_constituency_id = models.ForeignKey(Assembly_Constituencies, on_delete=models.CASCADE, 
                                    verbose_name='Assembly_Constituency',blank=True, null=True)"""
class Central_Legislatures(models.Model):
    name = models.CharField(max_length=100,blank = True)
    type = models.CharField(max_length=100,blank = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Central_Legislature"
        verbose_name_plural = "Central_Legislatures"


class State_Legislatures(models.Model):
    name = models.CharField(max_length=100,blank = True)
    type = models.CharField(max_length=100,blank = True)
    state_id = models.ForeignKey(States, on_delete=models.CASCADE, verbose_name='State')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "State_Legislature"
        verbose_name_plural = "State_Legislatures"

class Term(models.Model):
    term_name = models.CharField(max_length=100,blank = True)
    start_year = models.CharField(max_length=100,blank = True)
    end_year = models.CharField(max_length=100,blank = True)
    central_legislature_id = models.ForeignKey(Central_Legislatures, on_delete=models.CASCADE, verbose_name='Central_Legislatures')
    def __str__(self):
        return self.term_name
    class Meta:
        verbose_name = "Term"
        verbose_name_plural = "Terms"