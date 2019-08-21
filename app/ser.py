from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from  datetime import datetime,timedelta
from  .models import *
import yunpian
from .Yunpian import *

class VerCodeSer(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=11,min_length=11)
    class Meta:
        model = Verycode
        fields = ('tel',)

    # def create(self, validated_data):
    #     yun = Yunpian()
    #     code = yun.get_code()
    #     re_data = yun.send_code(validated_data['tel'],code)
    #     if re_data['code'] == 0:
    #         code_obj,create = Verycode.objects.\
    #             update_or_create(defaults={'code':code},
    #                                     tel=validated_data['tel'])
    #         return code_obj
    #     return ValidationError(re_data['msg'])
    def create(self, validated_data):
        yun = Yunpian()
        code = yun.get_code()
        re_data = yun.send_code(validated_data['tel'],code)
        if re_data['code'] == 0:
            code_obj,c = Verycode.objects.update_or_create(defaults={'code':code},
                                                           tel=validated_data['tel'])
            return code_obj
        raise ValidationError(re_data['msg'])

class RegSer(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=11,write_only=True)
    code = serializers.CharField(max_length=20,write_only=True)
    class Meta:
        model = User
        fields = ('username','password','pwd2','tel','code')
    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一样')
        ago = datetime.now()-timedelta(minutes=300)
        code_obj = Verycode.objects.filter(tel=attrs['tel'],
                                           code=attrs['code'],
                                           time__gte=ago)
        if not code_obj:
            raise ValidationError('验证码错误或者过期')
        del attrs['pwd2']
        del attrs['code']
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LogSer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user:
            if user.check_password(attrs['password']):
                return attrs
        raise ValidationError('用户密码错误无')
