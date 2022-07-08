import requests
import time
import json
from playsound import playsound
from bs4 import BeautifulSoup


# 本程序为美签slot查询(英国：伦敦，贝尔法斯特)，可以根据期望的日期和刷新频率来刷新美签slot(英国：伦敦，贝尔法斯特)。
# 本程序仅限英国美签slot查询，大家也可以照猫画虎修改成自己所在的国家美签申请中心。
# 作者Java刚转Python 1周，写个爬虫试试水。代码方面不够简洁，请谅解！
# 请勿用此程序提交恶意请求，本程序仅供学习使用，对于使用者的任何行为和造成的后果本作者不承担任何法律责任！
# 祝大家能够抢到自己心仪的的slot！


# authToken non-login session are needed for further login processes.(authToken和未登录时的session获取，为登录作准备)
def getInfo():
    with open('data.json', 'r') as dataFile:
        data = json.load(dataFile)
    userAgent = data['user-agent']

    headers = {
        'User-Agent': userAgent
    }
    session = requests.Session()
    response = session.get('https://ais.usvisa-info.com/en-gb/niv/users/sign_in', headers=headers).text

    preSession = session.cookies

    soup = BeautifulSoup(response, 'lxml')
    return soup.find_all('input')[1].attrs['value'], preSession, userAgent


# send login request, and gain cookie after login. (发送登录请求，获取登录后的cookie)
def login(email, password):
    response = getInfo()
    authToken = response[0]
    preSession = response[1]
    userAgent = response[2]

    name = ''
    value = ''
    for c in preSession:
        name = c.name
        value = c.value
    cookie = name + "=" + value

    payload = {
        'utf8': '✓',
        'user[email]': email,
        'user[password]': password,
        'policy_confirmed': '1',
        'commit': 'Sign In',
        'authenticity_token': authToken
    }

    # 请请求头尽可能模拟浏览器
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'ais.usvisa-info.com',
        'Origin': 'https://ais.usvisa-info.com',
        'Referer': 'https://ais.usvisa-info.com/en-gb/niv/users/sign_in',
        'Update-Insecure-Requests': '1',
        'User-Agent': userAgent,
        'Cookie': cookie
    }

    loginSession = requests.Session()

    loginResponse = loginSession.post('https://ais.usvisa-info.com/en-gb/niv/users/sign_in', headers=headers,
                                      data=payload)

    loginSessionName = ''
    loginSessionValue = ''

    for c in loginResponse.cookies:
        loginSessionName = c.name
        loginSessionValue = c.value
        break

    return loginSessionName + "=" + loginSessionValue


# 发生错误并重试
def retry():
    print('发生了一些错误或者会话过期，5秒后重试。。。')
    time.sleep(5)

    execute()

# 邮件推送
def sendMail(mailContent):
    with open('data.json', 'r') as dataFile:
        data = json.load(dataFile)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect(data['smtp_url'], data['smtp_port'])
    smtp.login(data['smtp_from_address'], data['smtp_password'])
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = data['smtp_from_address']
    msg['subject'] = 'Visa Slot'
    msg['to'] = data['smtp_to_address']
    txt=email.mime.text.MIMEText(mailContent,'HTML','utf-8')
    msg.attach(txt)
    smtp.sendmail(msg['from'],msg['to'],str(msg))

# 邮件推送
def mailGun(mailContent):
    with open('data.json', 'r') as dataFile:
        data = json.load(dataFile)
    return requests.post(
        "https://api.mailgun.net/v3/"+ data['mailgun_domain_name'] +"/messages",
        auth=('api', mailgun_api_key),
        data={"from": "船票Get <mailmaster@"+ data['mailgun_domain_name'] +">",
              "to": [data['mailgun_to_address']],
              "subject": "Visa Slot",
              "text": mailContent})

def execute():
    counter = 0

    # 读取 JSON文件
    with open('data.json', 'r') as dataFile:
        data = json.load(dataFile)
    # 邮箱地址
    email = data['email']
    # 密码
    password = data['password']
    # schedule ID可以在reschedule页面的URL找到
    scheduleID = data['scheduleID']
    # expected date 是在此日期之前的期望slot
    expectedDate = data['expectedDate']
    # 播放声音提醒有期望的slot。大家也可以删掉/改变播放声音部分/路径如果不喜欢
    notiSoundPath = data['notiSoundPath']
    # sleep时间，单位秒数
    sleepTime = data['sleep']
    # user-agent
    userAgent = data['user-agent']

    # 登录
    cookie = login(email, password)

    while True:

        try:
            # 请请求头尽可能模拟浏览器
            # construct headers (DO NOT MODIFY THESE REQUEST HEADERS IF YOU DON'T FAMILIAR WITH HTTP REQUEST 请勿随意修改请求头)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Cookie': cookie,
                'Connection': 'keep-alive',
                'Host': 'ais.usvisa-info.com',
                'Upgrade-Insecure-Requests': '1',

                # 如果输出错误/HTML代码，可能是User-Agent的问题。
                # User-Agent 根据不同的系统而不同，我用的是MacOS的User-Agent。
                # 如果在Windows运行，通常用：
                # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
                # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
                # Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
                # 这三个都可以。
                # 如果是MacOS，以下有几个通常用的例子：
                # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36
                # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
                # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
                #
                # 如果以上的例子乱码还会出现，那么就可以按照以下方法做：
                # 在浏览器打开F12切换到network栏，在签证官网刷新页面随便点一个request，下拉看到request
                # header里面的user - agent右键复制。然后在main.py里面把user - agent的值删除然后粘贴即可。

                'User-Agent': userAgent
            }

            londonSession = requests.Session()

            # send requests and get london and belfast schedule responses
            londonResponse = londonSession.get(
                "https://ais.usvisa-info.com/en-gb/niv/schedule/" + scheduleID + "/appointment/days/17.json?appointments[expedite]=false",
                headers=headers)

            belfastResponse = requests.get(
                "https://ais.usvisa-info.com/en-gb/niv/schedule/" + scheduleID + "/appointment/days/16.json?appointments[expedite]=false",
                headers=headers)
            print("时间: " + str(time.asctime()))

            # london slot check
            earliestLondon = londonResponse.text[10:20]
            print('London:')
            if len(londonResponse.text) == 2:
                print("呜呜呜伦敦slot都没有啦")
            elif earliestLondon == "Your sessi" or earliestLondon == "You need t":
                retry()
            elif earliestLondon > expectedDate:
                print('可预定但超过期望时间：' + earliestLondon)
                print('链接: ' + 'https://ais.usvisa-info.com/en-egb/niv/schedule/' + scheduleID + '/appointment')
            elif earliestLondon <= expectedDate:
                print('！！可预定！！London 最早可预定时间: ' + earliestLondon)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment')
                mailContent = '！！可预定！！London 最早可预定时间: ' + earliestLondon + '\n' + '链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment'
                if data['mail'] == 1:
                    sendMail(mailContent)
                if data['mailGun'] == 1:
                    mailGun(mailContent)
                playsound(notiSoundPath)
            else:
                retry()

            # belfast slot check
            earliestBelfast = belfastResponse.text[10:20]
            print('Belfast:')
            if len(belfastResponse.text) == 2:
                print("呜呜呜贝法slot都没有啦\n")
            elif earliestLondon == "Your sessi" or earliestLondon == "You need t":
                retry()
            elif earliestBelfast > expectedDate:
                print('可预定但超过期望时间：' + earliestBelfast)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment' + '\n')
            elif earliestBelfast <= expectedDate:
                print('！！可预定！！Belfast 最早可预定时间: ' + earliestBelfast)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment' + '\n')
                mailContent = '！！可预定！！Belfast 最早可预定时间: ' + earliestBelfast + '\n' + '链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment'
                if data['mail'] == 1:
                    sendMail(mailContent)
                if data['mailGun'] == 1:
                    mailGun(mailContent)
                playsound(notiSoundPath)
                # 播放声音，大家也可以删掉/改变播放声音部分如果不喜欢
                playsound(notiSoundPath)
            else:
                retry()

            # refresh cookie and store to JSON file
            # 循环counter次后更新session以保持登录状态，这里可以改刷新频率。但是请注意经过测试session过期时间大概为30分钟，刷新频率最好不要大于30min/次
            counter = counter + 1
            if counter == 10:
                londonCookie = londonResponse.cookies
                newLondonCookiePart = json.dumps(requests.utils.dict_from_cookiejar(londonCookie)).split("\"")[3]
                newLondonCookie = "_yatri_session=" + newLondonCookiePart
                cookie = newLondonCookie

                counter = 0

            # sleep time (少于5秒可能会造成TooManyRequests Error,建议sleep时间>=5秒)
            time.sleep(sleepTime)
        # catch errors and retry
        # 如果一些不可预测的bug发生,隔5秒重试。
        except Exception:
            traceback.print_exc()
            retry()


# 主函数
if __name__ == '__main__':
    execute()
