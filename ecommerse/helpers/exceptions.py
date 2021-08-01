from rest_framework.exceptions import  APIException


class PhoneNumberNotFoundException(APIException):
    status_code = 400
    default_detail = "Phone number not found."


class OTPCoolDownException(APIException):
    status_code = 400
    default_detail = "You can only resend OTP once in 60 seconds."


class MaxResendOTPLimitReached(APIException):
    status_code = 400
    default_detail = "Maximum limit of resending OTP reached."


class InvalidOTPException(APIException):
    status_code = 400
    default_detail = "The otp entered is invalid."


class InvalidTokenException(APIException):
    status_code = 400
    default_detail = "The token given is invalid."


class PhoneNumberExistsException(APIException):
    status_code = 400
    default_detail = "Phone number exists already."

