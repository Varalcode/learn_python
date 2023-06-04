# Importar las bibliotecas necesarias
from fpdf import FPDF
import datetime

# Solicitar una cadena de texto al usuario
texto_usuario = input("Ingrese una cadena de texto: ")

fecha_actual = datetime.date.today()
# Crear un objeto PDF personalizado


class PDF(FPDF):
    def header(self):
        # Configurar la cabecera del documento PDF
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Parte plana mayor', 0, 1, 'C')
        self.cell(0, 10, '28 - 05 - 2023', 0, 1, 'C')

    def footer(self):
        # Configurar el pie de página del documento PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, titulo):
        # Configurar el título del capítulo en el documento PDF
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, titulo, 0, 1, 'L')

    def chapter_body(self, texto):
        # Configurar el contenido del capítulo en el documento PDF
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, texto)
        self.ln()


# Crear un objeto PDF
pdf = PDF()

# Agregar una página al documento PDF
pdf.add_page()

# Agregar el título del capítulo
pdf.chapter_title("Cadena de texto ingresada")

# Agregar el contenido del capítulo (cadena de texto ingresada por el usuario)
pdf.chapter_body(texto_usuario)

# Guardar el documento PDF en un archivo
pdf.output("documento.pdf")
