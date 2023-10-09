from django.shortcuts import render
from website.forms import NameForm, ContactForm, NewsletterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'Unknown'
            form.save()
            messages.add_message(request, messages.SUCCESS,'Your ticket submitted seccessfully!')
        else:
            messages.add_message(request, messages.ERROR,'Your ticket didnt submitted!')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(name, subject, email, message)   
            form.save()                                   
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    # form = NameForm()
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


def all_urls_redirect(request):
    if settings.MAINTENANCE_MODE:
        return HttpResponseRedirect(reverse('maintenance_mode'))