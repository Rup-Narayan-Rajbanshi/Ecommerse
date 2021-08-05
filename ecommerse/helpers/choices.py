from .constants import OTP_TYPES, OTP_STATUS_TYPES, SIZE, GENDER, ORDER_STATUS, PRODUCT_STATUS

GENDER_CHOICES = (
    (GENDER['ALL'], 'All'),
    (GENDER['MALE'], 'Male'),
    (GENDER['FEMALE'], 'Female'),
    (GENDER['OTHER'], 'Other'),
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


SIZE_CHOICES = (
	(SIZE['SMALL'],"S"),
	(SIZE['MEDIUM'], "M"),
	(SIZE['LARGE'], "L"),
	(SIZE['XTRA_LARGE'],"XL"),
		)


PRODUCT_STATUS_CHOICES = (
    (PRODUCT_STATUS['ACTIVE'], 'Active'),
    (PRODUCT_STATUS['INACTIVE'], 'Inactive')
)


ORDER_STATUS_CHOICES = (
    (ORDER_STATUS['NEW_ORDER'], 'New Order'),
    (ORDER_STATUS['CONFIRMED'], 'Confirmed'),
    (ORDER_STATUS['SHIPPED'], 'Shipped'),
    (ORDER_STATUS['CANCELLED'], 'Cancelled'),
    (ORDER_STATUS['DELIVERED'], 'Delivered')
)





