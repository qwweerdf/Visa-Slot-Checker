# 使用教程

## 1. 确保已经安装python3 & pip3

python下载安装: https://www.python.org/downloads/ ,并且确保python已经加到环境变量中。

pip下载安装: https://pip.pypa.io/en/stable/installation/#get-pip-py 

## 2. 下载此项目

https://github.com/qwweerdf/Visa-Slot-Checker/archive/refs/heads/main.zip

## 3. 文件夹解压后打开终端(此目录)

### 1.安装所需库

```shell
pip install -r requirements.txt
```
### 2.填写JSON配置文件

#### 1.email & password

填写你的邮箱地址和密码。

#### 2.scheduleID

在schedule界面当中找到浏览器顶部URL有串8位数数字即scheduleID。

#### 3.expectedDate

期望日期：在此日期之前的期望slot日期，必须按照yyyy-mm-dd格式填写。

#### 4.notiSoundPath

提示音路径：可以保持默认也可以改成自己的路径。

#### 5.sleep

程序睡眠时间：少于5秒可能会造成TooManyRequests Error,建议sleep时间>=5秒。

#### 6.user-agent

每个人的电脑因为系统浏览器版本和配置都不同，所以每个人的user-agent也不相同，具体的获取方法如下：

方法一：访问 http://whatsmyuseragent.org/ 复制粘贴第一个框的内容到data.json里面的user-agent的值里面即可。

方法二：在Chrome/Firefox/Edge浏览器打开F12切换到network栏，在签证官网刷新页面随便点一个request，下拉看到request header里面的user-agent右键复制。然后在data.json里面把user-agent的值删除然后粘贴即可。

**-------------------------------------以下配置内容为可选-------------------------------------**

#### 7.playSound

是否播放声音，如果在服务器上运行并开启邮件提醒可关闭声音播放。

**-----------------SMTP-----------------**

#### 8.smtpMailSender

是否开启smtp邮件推送。

##### 8.1.smtp_url

smtp服务器地址

##### 8.2.smtp_port

smtp端口

##### 8.3.smtp_from_address

发送邮件的邮箱

##### 8.4.smtp_to_address

接受邮件的邮箱

##### 8.5.smtp_password

发送邮件的邮箱的密码

**-----------------MAIL GUN API-----------------**

#### 9.mailGunSender

是否开启mailgun邮件发送

##### 9.1.mailgun_domain_name

mailgun域名

##### 9.2.mailgun_api_key

mailgun private api key

##### 9.3.mailgun_to_address

接收邮件的地址

### 3.运行程序

```shell
python main.py
```

### 4.等待&抢

祝大家能够抢到自己心仪的的slot！

# 免责声明

请勿用此程序提交恶意请求，本程序仅供学习使用，对于使用者的任何行为和造成的后果本作者不承担任何法律责任！

# 额外信息

## 后续操作

配置完成并且能够正常运行之后之后，每次只需运行程序即可 -> python main.py。

## Windows可执行文件（过时，需要cookie）

大家可以在Windows系统中，解压zip文件（可以在右边的release里面找到），确保data.json，main.exe和noti.mp3在同一目录下。在配置完data.json之后直接双击执行main.exe文件。

## 已知可能出现的问题 

1. User-Agent错误识别

> 如果输出错误/HTML代码，可能是User-Agent的问题。
>
> 
> 如果在Windows运行，通常用：
> 
> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
> 
> Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
> 
> Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
> 
> 这三个都可以。
> 
> 如果是MacOS，以下有几个通常用的例子：
> 
> Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36
> 
> Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
> 
> Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
> 如果以上的例子乱码还会出现，那么就可以按照以下方法做：
> 
> 在浏览器打开F12切换到network栏，在签证官网刷新页面随便点一个request，下拉看到request header里面的user-agent右键复制。然后在main.py里面把user-agent的值删除然后粘贴即可。

# FAQs

### 1. 能否刷除了英国意外其他国家？

> 懂的小伙伴可以手动更改请求链接以及请求的城市代码并且配置好请求头的参数，只要官网是 ais.usvisa-info.com 道理都差不多。

### 2. 为什么出现乱码？

> 可能是请求头中user-agent的问题，请看填写JSON配置文件部分。请注意有些引号例如" "或者' '请勿删除！

### 3. data.json文件中的<>是否需要删除？

> 是的，data.json的email, password，scheduleID和user-agent都需要把<>删掉然后粘贴值到" "里面。

### 4. 程序会侵犯我的隐私吗？

> 所有的个人敏感信息都是需要在下载到本地进行配置的，本程序只是根据你的信息模仿你的浏览器发送http请求来刷新验证slot，不会窃取你的任何个人信息。

# 需要更多帮助？

电子邮箱：1563470117@qq.com