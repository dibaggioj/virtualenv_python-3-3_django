from django.shortcuts import render_to_response
from django.template.context import RequestContext
# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
# from django.shortcuts import render


def home(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('../templates/mysite/home.html',
                             context_instance=context)


# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request, 'mysite/contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''),
#     })
