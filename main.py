import requests
import time
import json
from playsound import playsound


# 本程序为美签slot查询(英国：伦敦，贝尔法斯特)，可以根据期望的日期和刷新频率来刷新美签slot(英国：伦敦，贝尔法斯特)。
# 本程序仅限英国美签slot查询，大家也可以照猫画虎修改成自己所在的国家美签申请中心。
# 作者Java刚转Python 1周，写个爬虫试试水。代码方面不够简洁，请谅解！
# 请勿用此程序提交恶意请求，本程序仅供学习使用，对于使用者的任何行为和造成的后果本作者不承担任何法律责任！
# 祝大家能够抢到自己心仪的的slot！

def inputCookie():
    newCookie = input("会话过期了/发生了一些错误，请输入新的Cookie值：")
    with open('data.json', 'r') as updatedDataFile:
        updateData = json.load(updatedDataFile)
    updateData['cookie'] = newCookie
    with open('data.json', 'w') as changedDatafile:
        json.dump(updateData, changedDatafile, indent=4)
    execute()


def execute():
    counter = 0

    while True:

        # 读取 JSON文件 (在运行过程中可以随时修改JSON文件，保存立即生效)
        with open('data.json', 'r') as dataFile:
            data = json.load(dataFile)
        # cookie具体值获取方法请看README
        cookie = data['cookie']
        # schedule ID可以在reschedule页面的URL找到
        scheduleID = data['scheduleID']
        # expected date 是在此日期之前的期望slot
        expectedDate = data['expectedDate']
        # 播放声音提醒有期望的slot。大家也可以删掉/改变播放声音部分/路径如果不喜欢
        notiSoundPath = data['notiSoundPath']
        # sleep时间，单位秒数
        sleepTime = data['sleep']

        try:
            # construct headers (DO NOT MODIFY THESE REQUEST HEADERS IF YOU DON'T FAMILIAR WITH HTTP REQUEST 请勿随意修改请求头)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-GB,en;q=0.9',
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
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/101.0.4951.64 Safari/537.36 '
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
                inputCookie()
            elif earliestLondon < expectedDate:
                print('！！可预定！！London 最早可预定时间: ' + earliestLondon)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment')
                playsound(notiSoundPath)
            else:
                print('可预定但超过期望时间：' + earliestLondon)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment')

            # belfast slot check
            earliestBelfast = belfastResponse.text[10:20]
            print('Belfast:')
            if len(belfastResponse.text) == 2:
                print("呜呜呜贝法slot都没有啦\n")
            elif earliestBelfast == "Your sessi" or earliestBelfast == "You need t":
                inputCookie()
            elif earliestBelfast < expectedDate:
                print('！！可预定！！Belfast 最早可预定时间: ' + earliestBelfast)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment' + '\n')
                # 播放声音，大家也可以删掉/改变播放声音部分如果不喜欢
                playsound(notiSoundPath)
            else:
                print('可预定但超过期望时间：' + earliestBelfast)
                print('链接: ' + 'https://ais.usvisa-info.com/en-gb/niv/schedule/' + scheduleID + '/appointment' + '\n')

            # refresh cookie and store to JSON file
            # 循环counter次后更新session以保持登录状态，这里可以改刷新频率。但是请注意经过测试session过期时间大概为30分钟，刷新频率最好不要大于30min/次
            counter = counter + 1
            if counter == 10:
                londonCookie = londonResponse.cookies
                newLondonCookiePart = json.dumps(requests.utils.dict_from_cookiejar(londonCookie)).split("\"")[3]
                newLondonCookie = "_yatri_session=" + newLondonCookiePart
                with open('data.json', 'r') as updatedDataFile:
                    updateData = json.load(updatedDataFile)
                updateData['cookie'] = newLondonCookie
                with open('data.json', 'w') as changedDatafile:
                    json.dump(updateData, changedDatafile, indent=4)
                counter = 0

            # sleep time (少于5秒可能会造成TooManyRequests Error,建议sleep时间>=5秒)
            time.sleep(sleepTime)

        # catch errors and update json file
        # 如果一些不可预测的bug发生了或者session过期了，用户可以手动输入session值。
        except:
            inputCookie()


# 主函数
if __name__ == '__main__':
    execute()
