from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth import logout
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Admin must activate the account
            user.save()
            return redirect('registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'posts/register.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')


from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/post_list.html', {'page_obj': page_obj})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_list')  # Change to your desired redirect URL after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, '../Cheesedawg/templates/main/../templates/main/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def post_list(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'posts/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            return redirect('post_list')  # Redirect to the post list or another page
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})

def index(request):
    return render(request, 'posts/index.html')