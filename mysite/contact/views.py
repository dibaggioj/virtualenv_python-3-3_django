from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import RequestContext


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'mysite/contact_form.html', {'form': form}, context_instance=RequestContext(request))

