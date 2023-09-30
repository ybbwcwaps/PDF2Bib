import requests
import utils



if __name__ == "__main__":
    pdf_path = "./example/s11704-023-2386-4.pdf"
    pdf = utils.Pdf2Ref(pdf_path)
    for i in pdf.title_list:
        print(i, end="\n\n.....................\n\n")
    # print(len(pdf.title_list))
        
