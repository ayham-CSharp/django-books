from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.



class book(models.Model):
    bookId = models.AutoField(primary_key=True)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='publisherm')
    bookEng=models.TextField(max_length=200)
    bookTitle = models.TextField(max_length=200)
    craeted_date= models.DateTimeField(default=timezone.now)
    bookName =models.CharField(max_length=50)
    bookImage=models.ImageField(upload_to='book/')
    bookYearsTearm= models.CharField(max_length=30)
    status =models.BooleanField(default=False)
    slug  =models.SlugField(blank=True,null=True,unique=True)
    bookLike = models.ManyToManyField(User,blank=True,related_name='likes')
    def __str__(self):
        return self.bookName
    def total_like(self):
     return self.bookLike.count()
    def save(self,*args,**kwargs):
        self.slug=slugify(self.bookEng)
        super(book,self).save(*args,**kwargs)
class comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    book = models.ForeignKey(book,on_delete=models.CASCADE,related_name='comments')
    bookNotes = models.TextField(max_length=200)
    craeted_date= models.DateTimeField(default=timezone.now)
    like = models.BooleanField(default=False)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commentsUser')
    def __str__(self):
        return self.bookNotes
    

