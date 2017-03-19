from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
from lobby.services import get_all_blogs, create_blogpost, get_blog, add_comment, create_comment, extract_tags
from lobby.forms import BlogPostForm, CommentForm


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
    blog = get_blog(blog_id)
    comments = blog.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            author_email = form.data.get('author_email')
            content = form.data.get('content')
            comment = create_comment(blogpost=blog, author_email=author_email, content=content)
            add_comment(blog, comment)


    return render(request, 'blog_info.html', locals())


