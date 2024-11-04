from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from post.models import Post
from django.shortcuts import resolve_url


#New post page
def newPostView(request: HttpRequest):
    #Create a new post with user input
    response = render(request, 'post/post.html')

    if request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"], picture=request.FILES["picture"])
        post.save()
        response = redirect('main:homeView')

    return response

#Post details page
def postDetailsView(request: HttpRequest, postid:int):

    post = Post.objects.get(pk=postid)

    return render(request, 'post/postDetails.html', context={"post":post})

#Update post page
def updatePostView(request: HttpRequest, postid:int):
    #Update an existing post with user input
    post = Post.objects.get(pk=postid)
    response = render(request, 'post/postUpdate.html', context={"post":post})

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "picture" in request.FILES: post.picture = request.FILES["picture"]
        post.save()    

        response = redirect('post:postDetailsView', postid=post.id)

    return response

#Delete post page
def deletePostView(request: HttpRequest, postid:int):
    #Delete an existing post
    post = Post.objects.get(pk=postid)
    post.delete()
    
    return redirect('main:homeView')
