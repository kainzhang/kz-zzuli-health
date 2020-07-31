# ZZULI 健康日报一键登记脚本

基于 Python3 + Selenium3 + Chrome + ChromeDriver，通过模拟点击和输入完成每日健康登记。可搭配定时任务程序实现自动登记。

## 前言

虽然已经是暑假，但每天的健康登记还要继续。为了不让班长和辅导员操心，也为了配合学校工作，所以现学现做尝试写了这个一键登记脚本。登记内容需要根据个人情况做调整，代码很简单，就是定位有点烦。

**需要已完成初次填写。不支持任何正常以外的选项，请按实际情况如实填写健康登记，根据个人情况自行修改**

暂不支持以下情况填写：
+ 到过湖北相关地区（包含停靠、停留、一直居住等方式）
+ 登记当日有发热、咳嗽、乏力等症状
+ 登记当日同住人员为疑似或确诊病例
+ 与疫区人员有过接触
+ 接触过疑似或确诊病例
+ 被当地要求到指定地点隔离
+ 曾经被诊断为确诊病例

PS：因为有点麻烦，就没写以上相关的内容。如果存在上述情况的请手动如实填写，愿疫情早日结束。另外由于错误填写带来的一切影响均由登记者本人承担。

**学校官网有时会网络不稳定导致登记超时，默认设定网页加载超过 30s 重试，最多重试 5 次，可自行修改。**

## 使用方法

本脚本基于 Python3 + Selenium3 + Chrome + ChromeDriver，请确保 PC 上有安装 Python3、Selenium、Chrome 以及配置了 ChromeDriver。Python3、Chrome 请从官网下载并安装。

确认已安装 Python 环境后，确认是否有安装 Selenium
```
pip show selenium
```

如未安装，在命令行输入如下语句安装 Selenium
```
pip install selenium
```

根据电脑已安装的 Chrome 版本（设置 -> 关于Chrome），在 [ChromeDriver 官网](http://chromedriver.chromium.org/) 下载版本号对应的 ChromeDriver（可能需要梯子）。解压文件并将 exe 文件拖入 Python 根目录的 Scripts 文件夹内；或者你个人为项目创建的 venv 虚拟环境的 Scripts 文件夹内。

以上配置完成后，编辑 `user_info.json` 文件，按照如下要求将信息替换为自己的，疫情期间到过的城市应修改为 `1`，如到过周口，则 `"zhoukou": 1`；`mail_flag` 为可选项，需要邮件发送结果则将值修改为 `1`，并配置邮箱信息。编辑完成后双击运行 `health_register.py` 即可；用 Python 相关 IDE 运行也可，注意配置环境。

``` json
  "username": "用户名，学号",
  "password": "信息门户密码",
  "dormitory_loc": "宿舍所在校区，科学：KX 走读：ZD",
  "dormitory_bd": "宿舍楼号，如 3 号楼填写 3",
  "dormitory_num": "宿舍号",
  "mobile_phone": "联系电话 11位手机",
  "home_phone": "家庭，家长电话",
  "xinyang": 0,
  "nanyang": 0,
  "zhumadian": 0,
  "shangqiu": 0,
  "zhoukou": 0,
  "other_info": "其他需要说明的情况",
  "mail_flag": 0
```

## 使用任务计划程序

可以使用 Windows 10 自带的任务计划程序实现每日定时自动登记。直接在搜索框搜索 `任务计划程序` 并打开，在 `操作` 选项中选择 `创建基本任务`，根据提示进行相关设置，执行操作为 `启动程序`，浏览文件并选择 `health_register.py` 作为执行脚本。然后等待指定时间自动运行即可。

## 使用邮件发送登记结果

在程序中可选择性使用邮箱提醒功能，将登记结果和时间发送至邮箱。
首先需要为邮箱开启 SMTP 服务，这里建议申请新邮箱作为发件邮箱。在邮箱设置中开启 `IMAP/SMTP` 服务，开启成功时会收到一个密码作为使用 SMTP 服务的密码。此外还需在邮箱设置页面找到邮箱提供的 SMTP 服务器地址。将上述信息及收件邮箱地址按照如下要求填写至 `user_info.json`，并同时将代码中的邮箱标记 `mail_flag` 修改为 `1`。

``` json
  "sender": "你的发件邮箱地址",
  "receiver": "你的收件邮箱地址",
  "smtp_pwd": "发件邮箱开通 SMTP 时提供的密码",
  "smtp_host": "发件邮箱 SMTP 服务器地址"
```
