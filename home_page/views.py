from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm , CommentForm
# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'pasword not matchcing...')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user.username)
            return redirect('/')
        else:
            messages.info(request, 'invalid credinatials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):

    auth.logout(request)
    return redirect('/')






   

# def post_detailview(request, id):
#     if request.method == 'POST':
#       cf = CommentForm(request.POST or None)
#     if cf.is_valid():
#       content = request.POST.get('content')
#       comment = Comment.objects.create(
#           posts=posts, user=request.user, content=content)
#       comment.save()
#       return redirect(posts.get_absolute_url())
#     else:
#       cf = CommentForm()

#     context = {
#         'comment_form': cf,
#     }
#     return render(request,"read_article.html", context)

def dashboard(request):
    user = request.user
    posts = Post.objects.filter(author=request.user)
    num_post = Post.objects.filter(author=request.user).count()

    print(user.username)
    return render(request, "dashboard.html", {'user': user, 'posts': posts, 'list': list, 'num_post': num_post})

# def dashboard(request):
#     # logged_in_user_posts = Post.objects.filter(User)
#     print(posts.title)

#     return render(request, 'dashboard.html', {'user': user,'posts':posts})


def posts(request, id):
    posts = Post.objects.get(id=id)
    user = posts.author
    return render(request, 'read_article.html', {'posts':posts,'id':id,'user':user})

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                body = form.cleaned_data['body']

                pst = Post(title=title, desc=desc, body=body)
                pst.author = request.user
                pst.save()
                form = PostForm()
                messages.info(request, 'Added sucessfully')
                return redirect('dashboard')

        else:
            form = PostForm()
        return render(request, 'add_post.html', {'form': form})


    else:
        return render(request, "login.html")


def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST or None, instance=pi,inital={'title':'hi'})
            if form.is_valid():
                form.save()

                messages.info(request, 'edited sucessfully')   
                return redirect('dashboard')

        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
        return render(request, 'edit_post.html', {'form': form})
      

    else:
        return render(request, "login.html")


def delete_post(request, id):
    if request.user.is_authenticated:
        post_to_delete = Post.objects.get(id=id)
        post_to_delete.delete()
        print('delete Sucessfully')
        messages.info(request,'delete sucessfully')
        return redirect('dashboard')

    else:
        return render(request, "login.html")


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})





def addcomment(request,id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.post = post
               comment.name = request.user

               comment.save()
               return redirect('posts', id=post.id)
               messages.info(request, 'Added sucessfully')

        else:
            comment_form = CommentForm()
        return render(request, 'add_comment.html', {'comment_form': comment_form})

    else:
        return redirect("login")
