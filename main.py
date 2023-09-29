import fitz
import requests
import re

def ExtractReferencesFromPdf(pdf_path):
    """从PDF文件中提取参考文献列表

    Args:
        pdf (path_to_pdf)
    """
    references = []
    pdf = fitz.open(pdf_path)
        


pdf_path = "./s11704-023-2386-4.pdf"
ExtractReferencesFromPdf(pdf_path)