import requests
import re
import utils
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from Ui_interface import *


class QtWindows(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.title_list=[]
        self.out_path = "./BIBs/"

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.OpenPDFFile.clicked.connect(self.openPdfFile)
        self.DownloadBIB.clicked.connect(self.downloadBib)

    def printf(self, my_str):
        self.OutPrint.append(my_str + '\n')   # Displays a prompt in the specified area
        self.cursor=self.OutPrint.textCursor()
        self.OutPrint.moveCursor(self.cursor.End)  # Move the cursor to the end so it will be displayed automatically
        QtWidgets.QApplication.processEvents()  

    def DoingPrint(self, info_str):
        self.Doing.clear()
        self.Doing.append("<font color='red'>" + info_str + "</font>")


    def openPdfFile(self):  
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self.centralwidget, "Select Pdf", "", "*.pdf;;All Files(*)")
            if file_path == "":
                self.DoingPrint("fileError: Can't open the file\n")
                return
            pdf = utils.Pdf2Ref(file_path)
            self.title_list = pdf.title_list
            self.OutPrint.clear()
            self.DoingPrint("以下是这篇PDF中的参考文献列表" + "...         点击按钮下载BIB格式文件")
            for i, title in enumerate(self.title_list):
                self.printf(f'{i+1}. {title}')
   
        except:
            self.OutPrint.clear()
            self.DoingPrint("fileError: Can't open the file\n")
            pass
        return
    
    def downloadBib(self):
        if self.title_list == []:
            self.OutPrint.clear()
            self.printf("Download Error: You haven't selected the PDF file")
            return
        url = f"https://dblp.org/search/publ/api?"
        self.DoingPrint("正在下载BIB文件, 请稍后......")
        self.OutPrint.clear()
        for title in self.title_list:            
            data = {        # Parameters to the get method
                'q': title,
                'format': 'bib'
            }
            response = requests.get(url, params=data)
            if response.status_code == 200:
                try:
                    title_match = re.search(r'title\s*=\s*{([^}]*)}', response.text)
                    t_name = re.sub(r'\n', '', (title_match.group(1)))
                    t_name = re.sub(r'\s+', ' ', t_name)
                except AttributeError:      # special precess
                    try:
                        title_new = title.replace('-', '')
                        data = {        
                            'q': title_new,
                            'format': 'bib'
                        }
                        response = requests.get(url, params=data)
                        title_match = re.search(r'title\s*=\s*{([^}]*)}', response.text)
                        t_name = re.sub(r'\n', '', (title_match.group(1)))
                        t_name = re.sub(r'\s+', ' ', t_name)
                    except:
                        self.OutPrint.clear()
                        self.printf("Failed: Can't find corresponding title")
                        if response.text == '':
                            continue
                        t_name = title
                with open(self.out_path+f"{title.replace(':', '').replace('?', '').replace('*', '')}.bib", 'w', encoding='utf-8') as bib_file:
                    self.printf(title)
                    bib_file.write(response.text)
                    self.printf("<font color='red'>" + "finished" + "</font>\n")
        
        self.printf("<font color='red'>" + "下载完成，所有文件都已经下载到 \"\\BIBs\\\" 文件夹下" + "</font>\n\n")
        self.DoingPrint("下载完成，所有文件都已经下载到 \"\\BIBs\\\" 文件夹下")
        

if __name__ == "__main__":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")    # Taskbar icon
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = QtWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())
