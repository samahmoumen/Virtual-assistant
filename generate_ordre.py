from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.utils import ImageReader

def app2(data, output_stream, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg'):
    c = canvas.Canvas(output_stream, pagesize=letter)
    width, height = letter

    # Add logo to the PDF
    try:
        logo = ImageReader(logo_path)
        logo_width = 100
        logo_height = 50
        logo_x = (width - logo_width) / 2  # Center the logo horizontally
        logo_y = height - logo_height - 20  # Position logo 20 units below the top of the page
        c.drawImage(logo, logo_x, logo_y, width=logo_width, height=logo_height)
    except Exception as e:
        print(f"Error adding logo: {e}")
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 150, "ORDRE DE MISSION")

    # Define styles for Paragraphs
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleN.fontName = 'Helvetica'
    styleN.fontSize = 12
    styleN.leading = 14  # Line height
    styleN.spaceBefore = 10  # Space before paragraph
    styleN.spaceAfter = 20  # Space after paragraph

    # Body text with spacing
    text_lines = [
        f"Nous avons une intervention à {data.get('lieu', '')}, Sur cela merci de donner au technicien {data.get('technicien', '')} un montant de {data.get('montant', '')} Dhs pour cette intervention il restera {data.get('duree', '')}.",
        "",  # Empty line for spacing
        "",  # Empty line for spacing
        "Demande par :",
        f"{data.get('demande_par', '')}"
    ]
    

    # Create a Frame to contain the paragraphs
    frame = Frame(72, 72, width - 144, height - 250, showBoundary=0)  # Adjusted margins

    # Convert text lines to Paragraphs
    paragraphs = [Paragraph(line, styleN) for line in text_lines]

    # Add Paragraphs to the Frame
    frame.addFromList(paragraphs, c)



    c.save()


