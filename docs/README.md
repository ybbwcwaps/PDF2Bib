# PDF2BIB
从英文文献PDF中提取参考文献，并下载所有的文献的 BIB 文件

## 从英文PDF中提取参考文献
利用 `PyMuPDF` 库(`import fitz`)来处理PDF文件[官方api参考](https://pymupdf.readthedocs.io/en/latest/document.html)。

想要利用`pdf.get_toc()`方法来获得`references`中的内容，但是有的文献pdf目录结构设置不正确，这种方法不能通用。

## 利用参考文献的信息从DBLP中获取 BIB 内容
从 DBLP 官网提供的获取文献 BIB 信息的 api：

[How to use the dblp search API?](https://dblp.org/faq/How+to+use+the+dblp+search+API.html)

使用 Python 的 `requests` 库，用 `get` 方法，传入 `q={文章标题}&format=bib` 即可查询到 BIB 格式的内容。