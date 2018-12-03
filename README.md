# 你的第一个项目：喝水小闹钟

## 项目概述 

这是你的第一个项目，你将要在这个项目中使用一个定时小闹钟，在繁忙的学习生活中提醒自己“生活不止眼前的苟且，还有诗和远方”。

给自己倒杯水，放首最喜欢的音乐，休息一下之后，继续为远方奋斗。

在这个项目中，你需要使用到课程中教授的string函数类，variables变量，并尝试自我学习list列表。


## 项目指南

### 步骤

1. 克隆存储库并打开下载的文件夹。

 ```	
git clone https://github.com/CheneyZeng/kivy_clock.git
```

2. 安装必要的 Python 依赖包


	对于 __Mac/OSX__：
	
	```bash
	conda env create -n my_python
	source activate my_python
	conda install ipykernel
	pip install -r require.txt
	python -m ipykernel install --user --name my_python --display-name "Python:my_python"
	```

	对于 __Windows__：
	
	```bash
	conda env create -n my_python
	activate my_python
	conda install ipykernel
	pip install -r require.txt
	python -m ipykernel install --user --name my_python --display-name "Python:my_python"
	```
	
3. 打开 notebook

```
jupyter notebook
```

4. 改变环境

[image1]: changekernel.png "Sample Output"

如图![Sample Output][image1]来kernel改成 **Python:my_python**。


__注意：__ 我们虽然已经实现了一些代码，让你更快地开始工作，你仍需要实现额外的功能，以回答 notebook 中所有的问题。
__除非有要求，否则不要修改任何已经包含的代码。__

## 项目评审

你的项目将会由优达学城的审阅者依据次项目的[评审标准](https://review.udacity.com/#!/rubrics/2398/view)进行审阅。请仔细阅读，并在提交之前自我评估你的项目。你必须通过了规则中的所有要求，才会审核通过。

## 项目提交

当你准备好提交你的项目时，将下列文件整理并压缩成一个文件，以便上传。

- 代码完整可运行的文件 `kivy_clock.ipynb`，所有的代码块都要执行并展示结果，并要求回答所有问题
- 将你的 notebook 导出为 HTML 以及 py 格式，并以 `kivy_clock.html` 以及 `kivy_clock.py` 命名
- 任何用于项目中，并且并非由我们为这一项目提供的额外数据图片。


