# PDF2Bib
基于 DBLP 官网提供的获取文献 BIB 信息的 api：

[How to use the dblp search API?](https://dblp.org/faq/How+to+use+the+dblp+search+API.html)

从PDF中解析出所有的参考文献，显示出来，并下载所有的文献的 BIB 文件

```
.   
├── README.md
├── Code
│   ├── background_rc.py
│   ├── main.py
│   ├── Ui_interface.py
│   ├── utils.py
├── resources
│   ├── background.jpg
│   ├── background.qrc
|	├── icon.ico
├── example
│   ├── *.pdf	# some pdf for test
├── run.bat
├── requirements.txt
```

运行需要的python库在[requirements.txt](./requirements.txt)中，并注意环境变量配置。

双击`run.bat`即可运行。

注意：如果你是在python的虚拟环境中运行该项目，请在`./Code/main.py`中加入你的虚拟环境中PyQt5路径，例如：

```python
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../myproject/Lib/site-packages/PyQt5/Qt5/plugins"
```

- 注意：相对路径要相对于你终端运行python代码的路经，
  例如：如果你在Code文件夹中终端运行`python main.py`，那么请写入相对于Code文件夹的路径；
  其它路径同理。

