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