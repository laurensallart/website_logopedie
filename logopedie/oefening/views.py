from django.shortcuts import render
from django.http import HttpResponse
from oefening.models import *
from oefening.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import sys

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    #if request.user:     
    child_list = get_children_list(request)
    context_dict = {'children': child_list}

    # Render the response and send it back!
    return render(request, 'oefening/index.html', context_dict)

@login_required
def child(request, child_userName_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        child = Child.objects.filter(user=request.user.id).get(slug=child_userName_slug)
        context_dict['child_userName'] = child.userName
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        resultaten = Resultaat.objects.filter(child=child)

        child_list = get_children_list(request)
        context_dict = {'children': child_list}

        # Adds our results list to the template context under name pages.
        context_dict['resultaten'] = resultaten
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['child'] = child
    except Child.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'oefening/child.html', context_dict)

@login_required
def add_child(request):
    context_dict={}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    # A HTTP POST?
    if request.method == 'POST':
        form = ChildForm(request.POST, request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            form = form.save(commit=False)
            if 'picture' in request.FILES:
                form.picture = request.FILES['picture']
            # Save the new category to the database.
            form.user = request.user
            form.save()
            

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ChildForm()
    context_dict['form']=form
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'oefening/add_child.html', context_dict)

@login_required
def add_opgave(request):
    context_dict={}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    if request.method == 'POST':
        form = OpgaveForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            if 'picture' in request.FILES:
                form.picture = request.FILES['picture']
            form.user = request.user
            form.save()

            return index(request)
        else:
            print form.errors

    else:
        form = OpgaveForm()
    context_dict['form']=form
    return render(request, 'oefening/add_opgave.html', context_dict)

@login_required
def add_reeks(request):
    context_dict={}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    if request.method == 'POST':
        form = ReeksForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            name = request.POST['name']
            form.user = request.user
            form.save()
            reeks=Oefeningenreeks.objects.filter(user=request.user).get(name=name)
            return add_opgave_to_reeks_view(request, reeks.slug)
        else:
            print form.errors

    else:
        form = ReeksForm()
    context_dict['form']=form

    return render(request, 'oefening/add_reeks.html', context_dict)

@login_required
def add_opgave_to_reeks_view(request, reeks_name_slug):
    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    try:
       
        reeks = Oefeningenreeks.objects.filter(user=request.user.id).get(slug=reeks_name_slug)
        context_dict['reeks_name'] = reeks.name
        print(reeks)
        
        
        opgaves_reeks = reeks.oefeningen.filter(user=request.user.id)
        opgaves_all = Opgave.objects.filter(user=request.user.id)
        opgaves_unused = opgaves_all.exclude(name__in=[str(o.name) for o in opgaves_reeks])
        # Adds our results list to the template context under name pages.
        context_dict['opgaves_unused'] = opgaves_unused

        context_dict['opgaves_reeks'] = opgaves_reeks
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['reeks'] = reeks
    except Oefeningenreeks.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        print('error')
        pass

    # Go render the response and return it to the client.
    return render(request, 'oefening/add_opgave_to_reeks_view.html', context_dict)

@login_required
def add_opgave_to_reeks(request, reeks_name_slug, opgave_name_slug):
    try:
        reeks=Oefeningenreeks.objects.filter(user=request.user.id).get(slug=reeks_name_slug)
        opgave=Opgave.objects.filter(user=request.user.id).get(slug=opgave_name_slug)
        reeks.oefeningen.add(opgave)
       

    except:
        print('error')
        pass
    return add_opgave_to_reeks_view(request, reeks_name_slug)

@login_required
def delete_opgave_from_reeks(request, reeks_name_slug, opgave_name_slug):
    try:
        reeks=Oefeningenreeks.objects.filter(user=request.user.id).get(slug=reeks_name_slug)
        opgave=Opgave.objects.filter(user=request.user.id).get(slug=opgave_name_slug)
        reeks.oefeningen.remove(opgave)
    except:
        print('error')
        pass
    return add_opgave_to_reeks_view(request, reeks_name_slug)

@login_required
def resultaten(request, child_userName_slug):
    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    try:
        child = Child.objects.filter(user=request.user.id).get(slug=child_userName_slug)
        context_dict['child_userName'] = child.userName

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        resultaten = Resultaat.objects.filter(child=child)

        # Adds our results list to the template context under name pages.
        context_dict['resultaten'] = resultaten
        context_dict['child'] = child
    except Child.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'oefening/resultaten.html', context_dict)

@login_required
def show_reeksen(request, child_userName_slug):
    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    try:
        child = Child.objects.filter(user=request.user.id).get(slug=child_userName_slug)
        print(child)
        context_dict['child']=child
        reeksen = Oefeningenreeks.objects.filter(user=request.user.id)
        print(reeksen)
        context_dict['reeksen']=reeksen
    except:
        print('error')
        pass

    return render(request, 'oefening/show_reeksen.html', context_dict)

@login_required
def start_oefening(request, child_userName_slug, reeks_name_slug):
    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    try:
        child = Child.objects.filter(user=request.user.id).get(slug=child_userName_slug)
        context_dict['child']=child
        reeks = Oefeningenreeks.objects.filter(user=request.user.id).get(slug=reeks_name_slug)
        context_dict['reeks']=reeks
        resultaat = Resultaat.objects.create(child=child, oefeningenreeks=reeks)
        context_dict['resultaat']=resultaat
        count=0
        resultaat_id=0
        context_dict['count']=count
        
        resultaat_id=resultaat.id
        return maak_oefening(request, child_userName_slug, reeks_name_slug, resultaat_id, count)
    except:
        e = sys.exc_info()[0]
        print(e)
        print('error 2')
        pass
    return index(request)
    #return index(request)

@login_required
def maak_oefening(request, child_userName_slug, reeks_name_slug, resultaat_id, count):
    count=int(count)
    

    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    child = Child.objects.filter(user=request.user.id).get(slug=child_userName_slug)
    context_dict['child']=child
    reeks = Oefeningenreeks.objects.filter(user=request.user.id).get(slug=reeks_name_slug)
    context_dict['reeks']=reeks
    opgave = reeks.oefeningen.all()[count]
    context_dict['opgave']=opgave
    resultaat = Resultaat.objects.get(id=resultaat_id)
    context_dict['resultaat']=resultaat
    context_dict['count']=count
    if request.method == 'POST':
        answer = request.POST.get('answer')
        
        answer_from_form= Answer.objects.create(child=child, opgave=opgave, answer=answer, correctAnswer=opgave.correctAnswer)
       
        resultaat.answers.add(answer_from_form)
        
        
        if int(answer_from_form.answer) == int(answer_from_form.correctAnswer):
            answer_from_form.correct = True
            answer_from_form.save()
            resultaat.grade=resultaat.grade+1
            
        resultaat.total=resultaat.total+1
        print(resultaat.grade)
        resultaat.save()
        print(resultaat.total)
        if count<(len(reeks.oefeningen.all())-1):
            count=count+1
            request.method='GET'
            return maak_oefening(request, child_userName_slug, reeks_name_slug, resultaat.id, count)
        elif count==(len(reeks.oefeningen.all())-1):
            resultaat.ended=True
            resultaat.save()
            request.method='GET'
            return index(request)
        #else:
         #   print(form.errors)
    #else:
        #form = AnswerForm()
    

    #context_dict['form']=form 
    return render(request, 'oefening/maak_oefening.html', context_dict)



    



def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'oefening/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/oefening/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'oefening/login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/oefening/')

@login_required
def get_children_list(request):
    children_list = Child.objects.filter(user=request.user.id)    
    return children_list

@login_required
def get_opgaves_list(request):
    opgaves_list = Opgave.objects.filter(user=request.user.id)
    return opgaves_list

@login_required
def opgaves(request):
    context_dict={}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    opgaves_list = get_opgaves_list(request)
    context_dict['opgaves']=opgaves_list
    return render(request, 'oefening/opgaves.html', context_dict)

@login_required
def reeksen(request):
    context_dict = {}
    child_list = get_children_list(request)
    context_dict = {'children': child_list}
    reeksen_list = Oefeningenreeks.objects.filter(user=request.user.id)
    context_dict['reeksen']=reeksen_list
    return render(request, 'oefening/reeksen.html', context_dict)




