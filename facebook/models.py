from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    city = models.CharField(max_length=100) 
    date = models.DateField()
    imageUrl = models.CharField(max_length=500,null=True)
    relationship = models.BooleanField(null=True)
    friends = models.ManyToManyField('self',blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


# class Group(models.Model):
#     name = models.CharField(max_length=100) 
#     descripton = models.CharField(max_length=200) 
#     owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
#     users =  models.ManyToManyField(User)

#     def __str__(self):
#         return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # group = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    body = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=500,null=True)
    likes = models.ManyToManyField(Profile)
    created = models.DateTimeField(auto_now_add=True)

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)
     
    # def __str__(self):
    #     return self.user
    
