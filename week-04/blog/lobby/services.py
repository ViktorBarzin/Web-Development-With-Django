from lobby.models import BlogPost, Comment, Tag, CommentAuthor


def get_all_blogs():
    return list(BlogPost.objects.all())


def create_blogpost(title, content, tags):
    import ipdb; ipdb.set_trace() # BREAKPOINT

    # Can throw exception if title > 255
    blog = BlogPost.objects.create(title=title, content=content)
    for tag in tags:
        blog.tags.add(tag)
    blog.save()



def get_blog(blog_id):
    blog = BlogPost.objects.filter(id=blog_id).first()
    if blog is None:
        raise ValueError('No blog with this id')
    return blog


def add_comment(blog, comment):
    blog.comments.add(comment)


def create_comment(*, blogpost, author_email, content, phone=None, fullname):
    # Need to validate input

    comment = Comment.objects.create(blogpost=blogpost, content=content)
    author = CommentAuthor.objects.create(fullname=fullname, email=author_email, phone=phone)
    author.comments.add(comment)
    author.save()

    comment.author = author
    comment.save()
    blogpost.comments.add(comment)

    return comment


def extract_tags(tags_string):
    # Tags are 1 string separated with space " "
    tags = []
    for tag in tags_string.split():
        tags.append(Tag.objects.create(name=tag))
    return tags

