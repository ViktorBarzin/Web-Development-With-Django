from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
from lobby.services import get_all_blogs, create_blogpost, get_blog, add_comment, create_comment, extract_tags
from lobby.forms import BlogPostForm, CommentForm, AuthorCommentModelForm


def index_view(request):
    blogposts = get_all_blogs()

    return render(request, 'index.html', locals())


def create_blogpost_view(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            title = form.data.get('title')
            content = form.data.get('content')
            # Creating tags
            tags_string = form.data.get('tags')
            tags = extract_tags(tags_string)
            create_blogpost(title, content, tags)
            return redirect(reverse('index'))
    return render(request, 'create_blogpost.html', locals())



def blogpost_info_view(request, blog_id):
    blogpost = get_blog(blog_id)

    comments = blogpost.comments.all()
    # form = CommentForm()
    form = AuthorCommentModelForm()
    if request.method == 'POST':
        # form = CommentForm(data=request.POST)
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


