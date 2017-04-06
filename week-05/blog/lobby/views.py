from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from lobby.services import get_all_blogs, create_blogpost, get_blog, add_comment, create_comment, extract_tags, get_all_public_posts
from lobby.forms import BlogPostModelForm, CommentForm, AuthorCommentModelForm


def index_view(request):
    if request.user.is_authenticated:
        blogposts = get_all_blogs()
    else:
        blogposts = get_all_public_posts()

    return render(request, 'index.html', locals())


@login_required(login_url=reverse_lazy('login'))
def create_blogpost_view(request):
    form = BlogPostModelForm()

    if request.method == 'POST':
        form = BlogPostModelForm(data=request.POST)

        if form.is_valid():
            title = form.data.get('title')
            content = form.data.get('content')
            # Creating tags
            tags_string = form.data.get('tags', '')
            tags = extract_tags(tags_string)
            is_private = True if form.data.get('is_private') == 'on' else False

            create_blogpost(title, content, tags, is_private)
            # form.save()
            return redirect(reverse('index'))
    return render(request, 'create_blogpost.html', locals())



def blogpost_info_view(request, blog_id):
    blogpost = get_blog(blog_id)

    comments = blogpost.comments.all()
    # form = CommentForm()
    form = AuthorCommentModelForm()
    if request.method == 'POST':
        form = AuthorCommentModelForm(data=request.POST)
        if form.is_valid():
            fullname = form.data.get('fullname')
            content = form.data.get('content')
            email = form.data.get('email')
            phone = form.data.get('phone')
            comment = create_comment(blogpost=blogpost, author_email=email, content=content, fullname=fullname, phone=phone)
            add_comment(blogpost, comment)
        # Setting data to {} to prevent refresh and spam with post
        form.data = {}


    return render(request, 'blog_info.html', locals())


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        # Logout
       logout(request)
       return redirect(reverse('login'))
    return render(request, 'profile.html', locals())

