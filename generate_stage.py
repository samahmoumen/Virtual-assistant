from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

def generate_pdf(data, output_stream, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg'):
    c = canvas.Canvas(output_stream, pagesize=letter)
    width, height = letter

    # Add logo to the PDF
    try:
        logo = ImageReader(logo_path)
        logo_width = 120  # Adjusted logo width
        logo_height = 80  # Adjusted logo height
        logo_x = (width - logo_width) / 2  # Center the logo horizontally
        logo_y = height - logo_height - 30  # Position logo 30 units below the top of the page
        c.drawImage(logo, logo_x, logo_y, width=logo_width, height=logo_height)
    except Exception as e:
        print(f"Error adding logo: {e}")

    # Add Company Information under the logo
    #c.setFont("Helvetica-Bold", 10)  # Smaller font for the company name
   # c.drawCentredString(width / 2, logo_y - 20, "Forges de Bazas")  # Position the text below the logo
    c.setFont("Helvetica", 8)  # Smaller font for the address
    c.drawCentredString(width / 2, logo_y - 20, "Lotissement Polygone, 13-14 & 15 Route des Zenata, Casablanca 20250")
    c.drawCentredString(width / 2, logo_y - 30, "Téléphone de l'entreprise : 05226-69850")

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 200, "Attestation de Stage")

    # Define styles for Paragraphs
    styles = getSampleStyleSheet()

    # Style for regular text
    styleN = ParagraphStyle(
        'Normal',
        fontName='Helvetica',
        fontSize=12,
        leading=18,  # Increased line spacing
        spaceBefore=10,
        spaceAfter=20,
    )

    # Style for dynamic text (italicized)
    styleItalic = ParagraphStyle(
        'Italic',
        parent=styleN,
        fontName='Helvetica-Oblique',
        textColor=colors.black,  # Black color for emphasis
    )

    # Body text with spacing and different font for dynamic data
    text_lines = [
        f"Nous, soussignés, Forges de Bazas, certifions par la présente que <i>{data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')}</i> a effectué un <i>{data.get('type_stage', '')}</i> au sein de notre entreprise du <i>{data.get('date_debut', '')}</i> jusqu'au <i>{data.get('date_fin', '')}</i>.",
        "",  # Empty line
        f"Durant cette période, <i>{data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')}</i> a été affecté au <i>{data.get('service', '')}</i>. Son intitulé de stage était : <i>{data.get('stage_intitule', '')}</i>.",
        f"<i>{data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')}</i> a fait preuve de plusieurs qualités professionnelles notamment rigueur, dynamisme et a su s’intégrer parfaitement à notre équipe.",
        "",
        "En foi de quoi, nous délivrons cette attestation pour servir et valoir ce que de droit.",
        "",
        f"Fait à Casablanca, le <i>{data.get('date_attestation', '')}</i>.",
        "",
        f"Nom et Prénom du Responsable : <i>{data.get('responsable_nom', '')}</i>",
        f"Titre du Responsable : <i>{data.get('responsable_titre', '')}</i>",
        "Signature :  "
    ]

    # Create a Frame to contain the paragraphs
    frame = Frame(72, 72, width - 144, height - 320, showBoundary=0)  # Adjusted margins and frame size

    # Convert text lines to Paragraphs
    paragraphs = [Paragraph(line, styleN) for line in text_lines]

    # Add Paragraphs to the Frame
    frame.addFromList(paragraphs, c)

    c.save()
