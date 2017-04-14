from lobby.models import BlogPost, Comment, Tag


def get_all_blogs():
    return list(BlogPost.objects.all())


def create_blogpost(title, content, tags):
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


def create_comment(*, blogpost, author_email, content):
    # Need to validate input

    comment = Comment.objects.create(blogpost=blogpost, author_email=author_email, content=content)
    blogpost.comments.add(comment)

    return comment


def extract_tags(tags_string):
    # Tags are 1 string separated with space " "
    tags = []
    for tag in tags_string.split():
        tags.append(Tag.objects.create(name=tag))
    return tags

