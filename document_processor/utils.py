from io import BytesIO
import json, re, subprocess
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template
from tika import parser
from xhtml2pdf import pisa
# from pyPDF import PdfFileReader

# importing required modules 
import PyPDF2 





def extract_pdf_invoice():
    raw = parser.from_file('uploads/invoices/invoice_read.pdf')
    print(raw['content'])


def pdf_to_text():
    #declare invoice params
    pdfFileObject = open('uploads/invoices/invoice_read.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        print(page.extractText())


def render_to_pdf(template_source, context_dict={}):
    print(context_dict)
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO() 
 
    #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def pdftojson():
    invoice_dir = os.path.join(settings.BASE_DIR, 'uploads', 'invoices')
    pdf_name = os.path.join(invoice_dir, 'INV001.pdf')
    output = subprocess.check_output(
        ['pdftotext', '-layout', pdf_name, '-']).decode()

    pages = output.strip('\f').split('\f')
    page  = pages[-1]

    address = re.search(r'(?s)(?<=from:).+?(?=\n\n)', pages[-1]).group()
    address = address.replace('For:', '').splitlines()

    sold_to, delivered_to = zip(
        *(re.split(r'\s{2,}', line.strip()) for line in address))

    bill_of_lading = re.search(r'Number:\s*(\S+)'    ,page).group(1)
    currency       = 'R'
    due_date       = re.search(r'Due:\s*(\S+)'          ,page).group(1)
    invoice_date   = re.search(r'Due Date:\s*(\S+)'      ,page).group(1)


    expenses = re.search(
        r'(?s)(amount*.+? Total\s*\S+)', page).group()
    expenses = re.sub(
        r'Amount', 'Amount', expenses)

    expenses = [
        re.split(r'\s{2,}', line.strip()) for line in expenses.splitlines()
    ]

    subtotal, tax, total = [
        expense[-1] for expense in expenses[-3:]
    ]

    summary = {
        'Sold To'       : sold_to,        'Delivered To'  : delivered_to, 
        'Bill of Lading': bill_of_lading, 'Currency'      : currency,
        'Due Date'      : due_date,
        'Invoice Number': invoice_number, 'Invoice Date'  : invoice_date,
        'Total'         : total,          'subtotal': subtotal,
        'tax' : tax
    }

    '''
    summary['Expenses'] = [
        dict(zip(expenses[0], expense)) for expense in expenses[1:-4]
    ]
    '''
    print(json.dumps(summary, indent=2, sort_keys=True))