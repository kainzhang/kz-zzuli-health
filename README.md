## 前言

ZZULI 每日健康登记一键登记脚本，半成品

虽然已经是暑假，但每天的健康登记还要继续。为了不让班长和辅导员大人操心，所以现学现做尝试写一键登记脚本。目前只根据我的需求写了初版，需要根据个人情况做另外的调整，代码也很简单，就是定位有点烦。

**暂不支持任何正常以外的选项，请按实际情况如实填写健康登记，根据个人情况自行修改**

## 使用方法

本脚本基于 Python3 + Selenium + ChromeDriver，请确保 PC 上有安装 Python3 和 Selenium。Python3 请从官网下载并安装。

确认已安装 Python 环境后，确认是否有安装 Selenium
```
pip show selenium
```

安装 Selenium
```
pip install selenium
```

根据电脑已安装的 Chrome 版本，在 [ChromeDriver 官网](http://chromedriver.chromium.org/) 下载对应的 ChromeDriver（可能需要梯子）。解压下载文件，将 exe 文件拖入 Python 根目录的 Scripts 文件夹内；或者你个人为项目创建的 venv 虚拟环境的 Scripts 文件夹内。

以上三项配置完成后，编辑文件，按照注释填写文件头部的内容。编辑完成后双击运行即可，用相关 IDE 运行也可。