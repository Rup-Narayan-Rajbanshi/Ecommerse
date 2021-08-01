from .constants import OTP_TYPES, OTP_STATUS_TYPES

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

OTP_TYPE_CHOICES = (
    (OTP_TYPES['USER_REGISTER'],'UserRegistration'),
    (OTP_TYPES['CHANGE_PASSWORD'],'ChangePassword'),
    (OTP_TYPES['CHANGE_PHONE_NUMBER'],'ChagePhoneNumber')
)

OTP_STATUS_CHOICES = (
    (OTP_STATUS_TYPES['ACTIVE'],'Active'),
    (OTP_STATUS_TYPES['INACTIVE'],'Inactive'),
    (OTP_STATUS_TYPES['EXPIRED'],'Expired')
)