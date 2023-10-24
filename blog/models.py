from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.model):
 """
 Database model for Posts including their title, content, author, and more.
 """
"""
on_delete=models.CASCADE ,check later to keep this or not,
"""
    title = models.Charfiels(max_length=250, unique=True)
    slug = models.SlugField(max_length=250 unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='colocar imagem aqui')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:

        """
        Posts oder's by date descending
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        returns number of likes
        """
        return self.likes.count()        

    class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        The order of comments by date ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns comment with body text and name
        """
        returnf"Comment{self.body} by {self.name}"    
