from UserInputs import UserInputs

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Times', 'B', 15)
        # Move to the right
        # self.cell(80)

        # Title
        self.cell(100, 10, "Summary of: " + UserInputs.outputTitle, ln = 1,
                    border = 0, align = 'L')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


# to be implemented for webinars/articles with photos
def gather_photos():
    return 0


def create_output():
    # from GeeksforGeeks

    # save FPDF() class into a
    # variable pdf
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_font('Times', '', 12)

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size = 12)

    UserInputs.output = UserInputs.output.replace('\n', '')
    # add another cell
    pdf.multi_cell(180, 10, txt = UserInputs.output,
                    align = 'J', border = 0)

    # save the pdf with name .pdf
    pdf.output("output.pdf")
