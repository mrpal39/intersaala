from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    
)
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import(
    authenticate,
    login,
    logout,
    )
from .forms import ProfileUpdateForm, SignUpForm,UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.decorators.csrf import csrf_exempt







def home_view(request):
    return render(request, 'home.html')


def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('account_login')
    else:
        return render(request, 'activation_invalid.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': '127.0.0.1:8000',
                # 'domain': current_site.domain,

                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def HomePage(request):

    return render(request, 'homepage.html')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        pass
def PasswordResetView(request):
    form = PasswordResetForm()
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
    

    return render(request, 'password_reset.html',{'form': form})


def logout_request(request):
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/')
    # form=log
@csrf_exempt
def login_request(request):
    form = AuthenticationForm(request=request, data=request.POST)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
        else:

            return HttpResponse(' an inv/alid login error message.')
            # return render (request ,'login.html', {'form':form})
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def student(request):
    std = students.objects.all().order_by('-pk')

    return render(request, 'create.html', {'std': std})


def student_list(request):

    if request.is_ajax and request.method == "POST":
        name = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        address = request.POST["address"]
        form = students.objects.create(
            name=name, last_name=lname, email=email, address=address)
        form.save()
        # messages.success(request, " Successfully logged in")
        # return HttpResponse("success")
        ser_instance = serializers.serialize('json', [form])

        # send to client side.
        return JsonResponse({"instance": ser_instance}, status=200)
    else:

        #         # some form errors occured.
        return JsonResponse({"error"}, status=400)

        # some form errors occured.

    # if request.is_ajax and request.method == "POST":

    # std=students.objects.all()

    #     ser_instance = serializers.serialize('json', [ std])

    #         # send to client side.
    #     return JsonResponse({"instance": ser_instance}, status=200)
    # else:
    #         # some form errors occured.
    #     return JsonResponse({"error"}, status=400)
    # return render(request,'stdlist.html',{'std':std})
# class updatestudent(UpdateView):


def update(request):
    if request.is_ajax and request.method == "POST":
        id = request.POST.get('sid')
        print(id)

        # upt=get_object_or_404(students,id=id)
        student = students.objects.get(id=id)
        student_data = {'id': student.id, 'name': student.name, 'lname': student.last_name,
                        'email': student.email, 'address': student.address, }

        return JsonResponse(student_data, status=200)
    #   else:

    # return render(request,'update.html',{'upt':upt})


def delete(request, id):

    delete_std = get_object_or_404(students, id=id)
    delete_std.delete()

    return HttpResponseRedirect('/')
