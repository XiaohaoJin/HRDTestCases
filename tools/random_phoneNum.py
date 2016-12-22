# coding: utf-8
'''
自动生成手机号码
'''
from random import choice


def random_PhoneNumber():
    try:
        area_number = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157', '158', '159', '187', '188', '130',
                '131', '132', '155', '156', '185', '186', '133', '153', '180', '189', '170', '177']
        area_number = choice(area_number)
        seed = '0123456789'
        sa = []
        for i in range(8):
            sa.append(choice(seed))
            last_eightNumber = ''.join(sa)
        phoneNum = area_number + last_eightNumber
        return phoneNum
    except:
        print('except_random_PhoneNumble')
    finally:
        print('finally_random_PhoneNumble')