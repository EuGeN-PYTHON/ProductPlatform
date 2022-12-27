from docx import *
from docx.shared import Inches

def get_path_document(request):
    pass

def load_document():
    pass

def make_document(id, ):

    document = Document()
    docx_title=f"Agreement№{id}.docx"
    # ---- Cover Letter ----
    # document.add_picture((r'%s/static/images/my-header.png' % (settings.PROJECT_PATH)), width=Inches(4))
    document.add_paragraph()
    document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))

    document.add_paragraph('Dear Sir or Madam:')
    document.add_paragraph('We are pleased to help you with your widgets.')
    document.add_paragraph('Please feel free to contact me for any additional information.')
    document.add_paragraph('I look forward to assisting you in this project.')

    document.add_paragraph()
    document.add_paragraph('Best regards,')
    document.add_paragraph('Acme Specialist 1]')
    document.add_page_break()

    # Prepare document for download
    # -----------------------------
    f = StringIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=' + docx_title
    response['Content-Length'] = length
    return response
