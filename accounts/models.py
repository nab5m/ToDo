from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models

class UsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w-_]\Z'
    message = '영문자, 숫자, _, -만 사용가능합니다.'


class UserProfile(AbstractUser):
    username = models.CharField("아이디", max_length=36, unique=True)
    username_validator = UsernameValidator()
    email = models.EmailField("이메일", max_length=255)

    address = models.CharField("도로명주소", max_length=255, blank=True, null=True)
    birth_date = models.DateField("생년월일", blank=True, null=True)
    phone = models.CharField("연락처", max_length=18, blank=True, null=True)
