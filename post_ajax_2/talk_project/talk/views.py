import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from talk.models import Post
from talk.forms import PostForm
from django.core.exceptions import ObjectDoesNotExist


def home(req):

    tmpl_vars = {
        'all_posts': Post.objects.reverse(),
        'form': PostForm()
    }
    return render(req, 'talk/index.html', tmpl_vars)


# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        response_data = {}

        post_text = request.POST.get('the_post')
        
        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def delete_post(request):
    if request.method == 'DELETE':
        response_data = {}

        try:
            post = Post.objects.get(pk=int(QueryDict(request.body).get('postpk')))
            post.delete()
            response_data['msg'] = 'Post was deleted.'
        except Post.DoesNotExist:  # from django.core.exceptions.ObjectDoesNotExist
            print("this post is no longer in the database")
            response_data['msg'] = 'Post could not be deleted. Post does not exist.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"noting to see": "this isn't happening"}),
            content_type="application/json"
        )
        
