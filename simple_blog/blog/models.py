from django.db import models


# A few fixed categories to keep the form simple (a dropdown instead of free text).
CATEGORY_CHOICES = [
    ('Technology', 'Technology'),
    ('Lifestyle', 'Lifestyle'),
    ('Education', 'Education'),
    ('Travel', 'Travel'),
    ('Personal', 'Personal'),
    ('Other', 'Other'),
]


class BlogPost(models.Model):
    """A single blog post / note."""

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Newest posts first

    def __str__(self):
        return self.title

    def short_description(self):
        """Return a short preview of the content for the home page cards."""
        if len(self.content) > 150:
            return self.content[:150] + '...'
        return self.content
