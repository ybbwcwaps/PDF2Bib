import fitz
import re

class Pdf2Ref:
    """Extract references from pdf
    """
    def __init__(self, pdf_path) -> None:
        self.pdf = fitz.open(pdf_path)
        self.references = ""
        self.ref_list=[]
        self.title_list=[]
        self.GetTitle()

    def GetRefPages(self):
        """Get the text content starting with references and following.
        """
        ref_list = []
        find = False
        for num, p in enumerate(self.pdf):
            content = p.get_text("blocks")
            for pc in content:
                if find:
                    ref_list.append(pc[4])
                else:
                    txtblocks = pc[4]
                    if "references" == txtblocks.lower().replace("\n", ""): # find references
                        find = True
        
        ref_list=[i.replace('\n',' ') for i in ref_list]
        references=' '.join(ref_list).replace('- ','-') # This is followed by a word wrap
        self.pdf.close()
        self.references = references
    

    def GetUnitRef(self):
        """Parse the text content into a single reference.
        """
        self.GetRefPages()
        pattern=re.compile(r'\[?[1-9][0-9]*\]?\.\s')
        ref_list=re.split(pattern,self.references)
        ref_list=list(filter(None,ref_list))
        self.ref_list = ref_list
    

    def GetTitle(self):
        """Get title form every reference.
        """
        self.GetUnitRef()
        for f in self.ref_list:
            # Use re library regular expression to split reference information
            keywords = ["\.","\?", "!", r'\([0-9]+\)']
            pattern = r"(" + r"|".join(keywords) + r")"
            sentences = re.split(pattern, f)

            self.title_list.append(re.sub(r'[\d\s]*$', '', (re.sub(r'\s+', ' ', sentences[2][:].replace('\n', ' ').lstrip().rstrip())) + "  "))# re.sub(r'\d*$', '', string)
        
