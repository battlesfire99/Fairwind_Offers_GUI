from fpdf import FPDF


class PDF(FPDF):
    font = "helvetica"

    def header(self):
        # Rendering logo:
        self.image("Fairwind_Header.png", 10, 10, 190)
        # Setting font: helvetica bold 15
        self.set_font(self.font, "B", 15)
        # Moving cursor to the right:
        self.cell(100)


    def footer(self):
        self.set_font(self.font, "I", 11)  # Setting font: helvetica italic 8
        self.set_text_color(96, 96, 96)
        self.set_y(-20)
        self.cell(80, 10, "Fairwind SA",0,0,"L",False)
        #Arguments : Width, Height, Text, Border (1) or no border (0), Next position of cursor (0 = right, 1 = beginning next line, 2 = below), Align (Left, center, right), Fill (False or True)

        self.set_y(-15)
        self.cell(80, 10, "BE 0893.326.646", 0, 0, "L", False)

        self.set_y(-20)
        self.cell(75)
        self.cell(80, 10, "299 Chaussée de Gilly", 0, 0, "c", False)
        # Arguments : Width, Height, Text, Border (1) or no border (0), Next position of cursor (0 = right, 1 = beginning next line, 2 = below), Align (Left, center, right), Fill (False or True)

        self.set_y(-15)
        self.cell(75)
        self.cell(80, 10, "6220 - Fleurus, Belgium", 0, 0, "c", False)

        self.set_y(-20)
        self.cell(180)
        self.cell(10, 10, "Page", 0, 2, "c", False)
        # Arguments : Width, Height, Text, Border (1) or no border (0), Next position of cursor (0 = right, 1 = beginning next line, 2 = below), Align (Left, center, right), Fill (False or True)

        self.set_y(-15)
        self.cell(183.5)
        #self.cell(10, 10, f"{self.page_no()}/{{nb}}", 0, 0, "R", False)
        self.cell(10, 10, f"{self.page_no()}/{{nb}}", 0, 0, "R", False)



    def coverPage(self):







# Instantiation of inherited class
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 410):
    pdf.cell(0, 10, f"Printing line number {i}", 0, 1)
pdf.output("tuto2.pdf")