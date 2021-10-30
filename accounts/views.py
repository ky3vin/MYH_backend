from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.models import AuthToken
#from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer #, ProfileSerializer
#from .models import Profile
#from django.contrib.auth.models import User
# from django.views.generic.detail import DetailView



from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Permission
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

#from django.contrib.auth.decorators import unauthenticated

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from rest_framework import generics
from rest_framework.reverse import reverse_lazy

#from .serializers import ProfileSerializer

from .tokens import account_activation_token
#from .models import Profile


@csrf_exempt
# Create your views here.
def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['student_ID']).exists():
            messages.info(request, 'error: 이미 존재하는 아이디입니다.')# 아이디 중복 체크
            return render(request, 'accounts/signup.html')
        if User.objects.filter(email=request.POST['email']).exists():
            messages.info(request, 'error: 이미 등록된 이메일입니다')#이메일 중복 체크
            return render(request, 'accounts/signup.html')
        #비밀번호 확인도 같다면
        if request.POST['password1'] == request.POST['password2']:
            # 유저 만들기
            user = User.objects.create_user(username=request.POST['student_ID'], email=request.POST['email'],
                                            password=request.POST['password1'], first_name=request.POST['phone_number'],
                                            last_name=request.POST['major'])
            user.is_active = False  # 유저 비활성화

            #permission = Permission.objects.create()
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화를 위한 확인 이메일입니다."
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect("home")  #####

        return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'accounts/signup.html')


def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서
        student_ID = request.POST['student_ID']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, username=student_ID, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect("home")  ##########
        # 실패
        else:
            return redirect("home")
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return render(request, 'accounts/login.html')  ####
    return render(request, 'home.html')


# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('home')  ###########
    else:
        return render(request, 'accounts/activate_error.html', {'error': '계정 활성화 오류'})



def home(request):
    return render(request, 'home.html')


class PasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset.html'
    mail_title = "비밀번호 재설정"

    def form_valid(self, form):
        return super().form_valid(form)


class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

def UserHome(request):
    return render(request, 'userHome.html')


# @unauthenticated_user
# def ForgotIDView(request):
#     context = {}
#     if request.method =='POST':
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#             if user is not None:
#                 template = render_to_string('accounts/email_template.html',)
#                 method_email = EmailMessage(
#                     '당신의 ID는 여기 있습니다.',
#                     str(user.username),
#                     settings.EMAIL_HOST_USER,
#                     [email],
#                 )
#             method_email.send(fail_silently=False)
#             return render(request, 'accounts/id_sent.html', context)
#         except:
#             messages.info(request, "이메일과 연동된 아이디가 존재하지 않습니다.")
#     context = {}
#     return render(request, 'accounts/forgot_id.html', context)

def member_modify(request):
    if request.method == "POST":
        user = User.objects
        user.first_name = request.POST["phone_number"]
        user.last_name = request.POST["major"]
        user.save()
        return redirect('home', request.user)
    return render(request, 'accounts/member_modify.html')


#
# class ProfileUpdateAPI(generics.UpdateAPIView):
#     lookup_field = "student_ID"
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer()

# from django.views.generic import UpdateView
# class handleUpdate(UpdateView):
#     model = Profile
#     fields = {'major'}
#     def get_object(self, queryset=):
#         return self.request.usernull
#     #queryset = Profile.objects.all()
#     #serializer_class = ProfileSerializer()

# from django.views.generic import DetailView
# from . import models as Model
# class user_profile(DetailView):
#     model = Profile
#     context_object_name = "user_obj"
#     template_name = "accounts/profile.html"
#     queryset = Profile.objects.all()






# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import auth
#
# # SMTP 관련 인증
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes, force_text
# from .tokens import account_activation_token
#
# # Create your views here.
# def signup(request):
#     # 포스트 방식으로 들어오면
#     if request.method == 'POST':
#         # 비밀번호 확인도 같다면
#         if request.POST['password1'] ==request.POST['password2']:
#             # 유저 만들기
#             user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#             user.is_active = False # 유저 비활성화
#             user.save()
#             current_site = get_current_site(request)
#             message = render_to_string('accounts/activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             mail_title = "계정 활성화 확인 이메일"
#             mail_to = request.POST["email"]
#             email = EmailMessage(mail_title, message, to=[mail_to])
#             email.send()
#             return redirect("home")
#
#     # 포스트 방식 아니면 페이지 띄우기
#     return render(request, 'accounts/signup.html')
#
#
#
# def login(request):
#     # 포스트 방식으로 들어오면
#     if request.method == 'POST':
#         # 정보 가져와서
#         username = request.POST['username']
#         password = request.POST['password']
#         # 로그인
#         user = auth.authenticate(request, username=username, password=password)
#         # 성공
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         # 실패
#         else:
#             return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
#     else:
#         return render(request, 'accounts/login.html')
#
# def logout(request):
#     # 포스트 방식으로 들어오면
#     if request.method == 'POST':
#         # 유저 로그아웃
#         auth.logout(request)
#         return redirect('home')
#     return render(request, 'accounts/signup.html')
#
# # 계정 활성화 함수(토큰을 통해 인증)
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         auth.login(request, user)
#         return redirect("home")
#     else:
#         return render(request, 'home.html', {'error' : '계정 활성화 오류'})
#     return
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # from rest_framework import viewsets, permissions, generics, status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.decorators import api_view
# # from knox.models import AuthToken
# # from .serializers import CreateUserSerializer, LoginUserSerializer, ProfileSerializer, UserSerializer
# # from .models import Profile
# # from django.contrib.auth.models import User
# # from django.views.generic.detail import DetailView
# #
# #
# #
# # # Create your views here.
# # @api_view(["GET"])
# # def HelloAPI(request):
# #     return Response("hello world!")
# #
# #
# # class RegistrationAPI(generics.GenericAPIView):
# #     serializer_class = CreateUserSerializer
# #
# #     def post(self, request, *args, **kwargs):
# #         if len(request.data["username"]) < 6 or len(request.data["password"]) < 4 or len(request.data["email"]) < 10:
# #             body = {"message": "너무 짧습니다"}
# #             return Response(body, status=status.HTTP_400_BAD_REQUEST)
# #         serializer = self.get_serializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         user = serializer.save()
# #
# # #########추가
# # #    def update_profile(request, student_ID):
# #  #       user = User.objects.get(student_ID=student_ID)
# #   #      user.save()
# #
# #         ###############
# #         #user.is_active = False
# #         #user.save()
# #         ###############
# #
# #
# #         return Response(
# #             {
# #                 "user": UserSerializer(
# #                     user, context=self.get_serializer_context()
# #                 ).data,
# #                 "token": AuthToken.objects.create(user)[1],
# #             }
# #         )
# #
# #
# # class LoginAPI(generics.GenericAPIView):
# #     serializer_class = LoginUserSerializer
# #
# #     def post(self, request, *args, **kwargs):
# #
# #         serializer = self.get_serializer(data=request.data)
# #
# #
# #         # if serializer.is_valid():
# #         #     serializer.save()
# #         #     return Response(serializer.data, status=status.HTTP_200_OK)
# #         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #         serializer.is_valid(raise_exception=True)
# #
# #         user = serializer.validated_data
# #         return Response(
# #             {
# #                 "user": UserSerializer(
# #                     user, context=self.get_serializer_context()
# #                 ).data,
# #                 "token": AuthToken.objects.create(user)[1]
# #
# #                 }
# #         )
# #
# #
# # class UserAPI(generics.RetrieveAPIView):
# #     permission_classes = [permissions.IsAuthenticated]
# #     serializer_class = UserSerializer
# #
# #     def get_object(self):
# #         return self.request.user
# #
# #
# # class ProfileUpdateAPI(generics.UpdateAPIView):
# #     lookup_field = "username"
# #     queryset = Profile.objects.all()
# #     serializer_class = ProfileSerializer()
# #
# #
# #
# # # class SignUp(APIView):
# # #     def post(self, request):
# # #         """
# # #         사용자 데이터 생성
# # #         """
# # #         serializer = UserSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_200_OK)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # #
