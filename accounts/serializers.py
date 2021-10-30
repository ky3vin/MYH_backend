# from rest_framework import serializers
# from django.contrib.auth.models import User, Permission
# from django.contrib.auth import authenticate
#
#
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string
# #from .models import User
# from .tokens import account_activation_token
# #from utils.common.cipher import AESCipher
#
# # 회원가입
# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password", "email")
#         #원래 맨앞"id"였음
#         extra_kwargs = {"password": {"write_only": True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             #validated_data["username"], None, validated_data["password"]
#             validated_data["username"], None, validated_data["password"]
#         )
#         #return user
#
#         permission = Permission.objects.create()
#         user.save()
#         current_site = get_current_site(self.context['request'])
#         message = render_to_string('accounts/activation_email.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': account_activation_token.make_token(user)
#             })
#
#         mail_subject = '계정활성화를 위한 이메일입니다'
#         to_email = validated_data["email"]
#             #EmailMessage(제목, 본문, 받는이)
#         email = EmailMessage(mail_subject, message, to=[to_email])
#         email.send()
#     return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
#         #     # 포스트 방식 아니면 페이지 띄우기
# return user
#
#
#
#         ######
#
#         ###################
#         #user.is_active = False
#         #user.save()
#         ####################
#
#
#
#
# # 접속 유지중인지 확인
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username")
#     #     #######원래 id임 student_ID는 추가한거
#     # class Meta:
#     #      model = User
#     #      field = '__all__'
#
# # 로그인
# class LoginUserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         ##원래는 return user
#         raise serializers.ValidationError("입력이 올바르지 않습니다. 다시 입력해주세요.")

#프로필 시리얼라이저
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ("major", "phone")




# class UserSerializer(serializers.ModelSerializer):
#     created_by = serializers.CharField(max_length=64, required=False)
#     updated_by = serializers.CharField(max_length=64, required=False)
#
#     class Meta:
#         model = User
#         field = '__all__'
#
#     def to_internal_value(self, data):
#         """
#         Post/Put과 같이 데이터 변경이 있을 때 데이터를 저장하기 전에 핸들링 할 수 있는 함수
#         """
#         ret = super(UserSerializer, self).to_internal_value(data)
#         return ret
#         #비밀번호를 암호화하기 위한 과정은 생략했음
#
#     def to_representation(self, obj):
#         """
#         GET/POST/PUT과 같이 데이터 변경 후 serializers.data로 접근할 때 값을 보여줌
#         """
#         ret = super(UserSerializer, self).to_representation(obj)
#         return ret
#
#     def validate_mail(self, value):
#         """
#         이메일이 데이터베이스에 존재하는지 확인
#         """
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("이메일이 이미 존재합니다.")
#         return value
#
#     def validate_password(self, value):
#         """
#         패스워드가 8글자 이하인지 확인
#         """
#         if len(value) < 8:
#             raise serializers.ValidationError("패스워드는 최소 %s자 이상이어야합니다." % 8)
#         return value
#
#     def create(self, validated_data):
#         """
#         데이터를 저장할 때 필요한 과정 구현
#         """
#         user = User.objects.create(
#             email=validated_data['username'],
#             password=validated_data['password'],
#         )
#         user.active = False
#         user.save()
#
#         #current_site = get_current_site(self.context['request'])
#         message = render_to_string('user/account_activate_email.html', {
#             'user': user,
#             'domain': 'localhost:8000',
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
#             'token': account_activation_token.make_token(user)
#         })
#
#         """
#         이메일 전송 과정
#         """
#         mail_subject = 'test'
#         to_email = 'kiy6410yt@gmail.com'
#         #EmailMessage(제목, 본문, 받는이)
#         email = EmailMessage(mail_subject, message, to=[to_email])
#         email.send()
#
#         return validated_data