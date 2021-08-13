from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 16)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Conservational Audit', 0, 0, 'C')
        # Line break
        self.ln(20)

def generate_pdf(title, version, description, img_name="", approvers=[]):
    title = f"{title.upper()}_V{version}"
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Times', '', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.set_font('Times', '', 14)

    pdf.cell(0, 10, "Description:", 0, 1)
    pdf.set_font('Times', '', 12)
    n = 130
    height = 0
    description = [description[i:i+n] for i in range(0, len(description), n)]
    for line in description:
        pdf.cell(0, 10, line, 0, 1)
        height += 10
    pdf.set_font('Times', '', 14)
    pdf.cell(0, 10, "Approvers:", 0, 1)
    for email in approvers:
        pdf.cell(0, 10, email, 0, 1)
        height += 10
    pdf.add_page()
    pdf.image(img_name, x = 5, y = 30, w = 200, h = 150, type = 'jpg')
    return pdf.output(title + '.pdf', 'F')

title = 'report1'
version = 1
description = 'this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report this is a test report test report' * 3
approvers = ['jeffcx416@gmail.com', 'xc1008@nyu.edu']
img_name = "img.jpg"
generate_pdf(title, version, description, img_name, approvers)



