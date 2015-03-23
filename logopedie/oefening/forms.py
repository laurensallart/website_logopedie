from django import forms
from oefening.models import *
from django import forms
from django.contrib.auth.models import User

class ChildForm(forms.ModelForm):
    userName = forms.CharField(max_length=128, help_text="Please enter a username.")
    firstName = forms.CharField(max_length=128, help_text="Please enter the first name.")
    lastName = forms.CharField(max_length=128, help_text="Please enter the last name.")
    age = forms.IntegerField(help_text="Please enter the age of the child")
    picture = forms.ImageField(widget=forms.FileInput(),required=False, help_text='Choose a profile picture')
    slug = forms.SlugField(widget=forms.HiddenInput(),required=False)

    

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        exclude = ('user',)
        model = Child
        fields = ('userName','firstName','lastName','age','picture')


class OpgaveForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter a name')
    question = forms.CharField(max_length=256, help_text='What is the question?')
    picture = forms.ImageField(widget=forms.FileInput(), required=False, help_text='Choose a profile picture')
    optie1 = forms.CharField(max_length=128, help_text='Add an option' )
    optie2 = forms.CharField(max_length=128, help_text='Add an option' )
    optie3 = forms.CharField(max_length=128, help_text='Add an option' )
    optie4 = forms.CharField(max_length=128, help_text='Add an option' )
    correctAnswer = forms.IntegerField(help_text='Choose the number of the correct answer above')
    difficultyOptions = (
        ('0', 'Easy'),
        ('1', 'Medium'),
        ('2', 'Hard'),
    )
    categoryOptions = (
        ('1', 'Woordenschat'),
        ('2', 'Bijwoorden'),
        ('2', 'Ander')
    )
    category = forms.ChoiceField(widget=forms.RadioSelect, choices= categoryOptions, help_text='what is the category?')
    
    difficulty = forms.ChoiceField(widget=forms.RadioSelect, choices= difficultyOptions, help_text='choose a difficulty')
    slug = forms.SlugField(widget=forms.HiddenInput(),required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        exclude = ('user',)
        model = Opgave
        fields = ('name','question','picture','optie1','optie2','optie3','optie4','correctAnswer','category','difficulty')

class AnswerForm(forms.ModelForm):
    class Meta:
        exclude = ('child', 'opgave', 'answer', 'correctAnswer',)
        model = Answer

class ReeksForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter a name')
    oefeningen = forms.CharField(required=False, widget=forms.HiddenInput())
    slug = forms.SlugField(widget=forms.HiddenInput(),required=False)

    class Meta:
        exclude = ('user',)
        model = Oefeningenreeks
        fields = ('name', 'oefeningen')

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text='userName')
    email = forms.CharField(max_length=128, help_text='email')
    password = forms.CharField(widget=forms.PasswordInput(), help_text="password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(),required=False, help_text='Choose a profile picture')
    class Meta:
        model = UserProfile
        fields = ('picture',)

