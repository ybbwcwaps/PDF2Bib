import requests
import re
import utils
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from Ui_interface import *

# Inheriting interface base classes to implement functionality
class QtWindows(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.title_list = []
        self.out_path = "./BIBs/"

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # Button click connect function
        self.OpenPDFFile.clicked.connect(self.openPdfFile)
        self.DownloadBIB.clicked.connect(self.downloadBib)

    def printf(self, my_str):
        # Displays a prompt in the specified area
        self.OutPrint.append(my_str + '\n')
        self.cursor = self.OutPrint.textCursor()
        # Move the cursor to the end so it will be displayed automatically
        self.OutPrint.moveCursor(self.cursor.End)
        QtWidgets.QApplication.processEvents()

    def DoingPrint(self, info_str):
        # A separate line is displayed
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
            self.DoingPrint(
                "fileError: Can't open the file Or It's not an English paper\n")
            pass
        return

    def downloadBib(self):
        if self.title_list == []:
            self.OutPrint.clear()
            self.Doing.clear()
            self.DoingPrint(
                "Download Error: You haven't selected the PDF file")
            return
        url = f"https://dblp.org/search/publ/api?"
        self.DoingPrint("正在下载BIB文件, 请稍后......")
        self.OutPrint.clear()
        for i, title in enumerate(self.title_list):
            self.printf(f"{i+1}. {title}")
            if re.search(r'(https?|ftp)://[^\s/$.?#].[^\s]*', title):   # is a URL
                self.printf("<font color='red'>" + "Warning: This is a URL!" + "</font>\n")
                continue
            data = {        # Parameters to the get method
                'q': title,
                'format': 'bib'
            }
            response = requests.get(url, params=data)
            if response.status_code == 200:
                # The following is to obtain the standard title
                try:
                    title_match = re.search(
                        r'title\s*=\s*{([^}]*)}', response.text)
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
                        title_match = re.search(
                            r'title\s*=\s*{([^}]*)}', response.text)
                        t_name = re.sub(r'\n', '', (title_match.group(1)))
                        t_name = re.sub(r'\s+', ' ', t_name)
                    except:
                        self.printf(
                            "<font color='red'>" + "Failed: Can't find corresponding title" + "</font>\n")
                        if response.text == '':
                            continue
                        t_name = title
                # The file name cannot contain illegal characters
                with open(self.out_path+f"{title.replace(':', '').replace('?', '').replace('*', '')}.bib", 'w', encoding='utf-8') as bib_file:
                    # self.printf(f"{i+1}. {title}")
                    bib_file.write(response.text)
                    self.printf("<font color='red'>" +
                                "Success!" + "</font>\n")
            else:
                # Network connection problem
                self.DoingPrint(
                    "<font color='red'>" + "Error: Please check your Internet connection" + "</font>\n")

        self.printf("<font color='red'>" +
                    "下载完成，所有文件都已经下载到 \"\\BIBs\\\" 文件夹下" + "</font>\n\n")
        self.DoingPrint("下载完成，所有文件都已经下载到 \"\\BIBs\\\" 文件夹下")


if __name__ == "__main__":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "myappid")    # Taskbar icon
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = QtWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
