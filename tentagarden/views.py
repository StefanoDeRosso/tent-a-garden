from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tentagarden.forms import UserForm, UserProfileForm

def home(request):
	context = RequestContext(request)
	
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				
			profile.save()
			
			registered = True
			
		else:
			print user_form.errors, profile_form.errors
			
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render_to_response(
			'tentagarden/home.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context)

def user_login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your Tent a garden account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
			
	else:
		return render(request, 'tentagarden/login.html', {})
		
@login_required
def user_logout(request):
	logout(request)
	
	return HttpResponseRedirect('/')


def list(request):
	# Handle file upload
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = File(docfile = request.FILES['docfile'])
			newdoc.save()
			
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('tentagarden.views.list'))
	else:
		form = FileForm() # A empty, unbound form
		
	# Load documents for the list page
	documents = File.objects.all()
	
	# Render list page with the documents and the form
	return render_to_response(
		'tentagarden/list.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)
