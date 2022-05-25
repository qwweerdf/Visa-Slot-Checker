# 使用教程

## 1. 确保已经安装python3 & pip

## 2. 下载此项目

https://github.com/qwweerdf/Visa-Slot-Checker/archive/refs/heads/main.zip

## 3. 文件夹解压后打开终端(此目录)

### 1.安装所需库

```shell
pip install -r requirements.txt
```
### 2.填写JSON配置文件

#### 1.cookie

cookie可以在登录之后的任何请求中获取。

例如：在reschedule界面按F12然后点击刷新，在第一个appointment请求中的请求/响应头找Cookie，右键复制即cookie。

#### 2.scheduleID

在schedule界面当中找到浏览器顶部URL有串8位数数字即scheduleID。

#### 3.expectedDate

期望日期：在此日期之前的期望slot日期，必须按照yyyy-mm-dd格式填写。

#### 4.notiSoundPath

提示音路径：可以保持默认也可以改成自己的路径。

#### 5.sleep

程序睡眠时间：少于5秒可能会造成TooManyRequests Error,建议sleep时间>=5秒。

### 3.运行程序

```shell
python main.py
```

### 4.等待&抢

祝大家能够抢到自己心仪的的slot！

# 免责声明

请勿用此程序提交恶意请求，本程序仅供学习使用，对于使用者的任何行为和造成的后果本作者不承担任何法律责任！

# 额外信息

## Windows可执行文件（懒人/小白）

如果大家还是不会配置环境，大家可以在Windows系统中，解压zip文件（可以在右边的release里面找到），确保data.json，main.exe和noti.mp3在同一目录下。在配置完data.json之后直接双击执行main.exe文件。

## 已知可能出现的问题 

1. User-Agent错误识别

> 如果输出错误/HTML代码，可能是User-Agent的问题。
> 
> User-Agent 根据不同的系统而不同，我用的是MacOS的User-Agent。
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

2. Windows可执行文件

> 在执行main.exe文件之后系统可能会出现延迟。在这种情况下，大家可以把sleep时间改为0以减少延迟时间。