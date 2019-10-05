from .models import UserProfile
import random

# 工具函数集

def getNewUid():
	template = "0123tuvwQRSBFG789ncdJKANOjkloPYZXefghipCDUVWq6_@^!Ex45MTHIabmLrsyz"
	num = random.randint(18,25)
	a = ''.join(random.choice(template) for x in range(num))
	userprofile = UserProfile.objects.filter(uid = a)
	if userprofile:
		return getNewUid()
	return a