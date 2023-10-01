import requests
import re
import utils


def downloadBib(title_list, out_path):
    url = f"https://dblp.org/search/publ/api?"
    for title in title_list:
        print(title)
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
                    print("Failed: Can't find corresponding title")
                    if response.text == '':
                        continue
                    t_name = title

            with open(out_path+f"{title.replace(':', '').replace('?', '').replace('*', '')}.bib", 'w', encoding='utf-8') as bib_file:
                print(f"Downloading the BIB of {t_name} ......")
                bib_file.write(response.text)
                print("finished")




if __name__ == "__main__":
    pdf_path = "./example/s11704-023-2386-4.pdf"
    pdf = utils.Pdf2Ref(pdf_path)
    # for i in pdf.title_list:
    #     print(i, end="\n\n.....................\n\n")
    # print(len(pdf.title_list))
    out_path = "./BIBs/"
    downloadBib(pdf.title_list, out_path)
