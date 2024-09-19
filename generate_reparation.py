from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch

def generate_pdf(data, pieces, output_stream, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg'):
    c = canvas.Canvas(output_stream, pagesize=letter)
    width, height = letter

    # Add logo to the PDF (centered)
    logo = ImageReader(logo_path)
    c.drawImage(logo, width / 2 - 50, height - 100, width=100, height=50)  # Centering the logo

    # Title
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 140, "FORGES DE BAZAS")

    # Date
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.red)
    c.drawCentredString(width / 2, height - 160, f"{data['date']}")

    # Personal Info
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(72, height - 180, "Nom :")
    c.setFillColor(colors.red)
    c.drawString(150, height - 180, f"{data['nom']}")
    c.setFillColor(colors.black)
    c.drawString(72, height - 220, "Client :")
    c.setFillColor(colors.red)
    c.drawString(150, height - 220, f"{data['client']}")
    c.setFillColor(colors.black)
    c.drawString(72, height - 240, "PDR Concernés :")
    c.setFillColor(colors.black)
    c.drawRightString(width - 285, height - 200, "Date de livraison chez client et mise en service :")
    c.setFillColor(colors.red)
    c.drawRightString(width - 220, height - 200, f"{data['date_livraison']}")

    # Draw the table of pieces
    table_data = [["REF", "DESIGNATIONS", "QTE", "N° SERIE"]] + pieces
    table = Table(table_data, colWidths=[1.5*inch, 3*inch, 0.5*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.red),  # Set the text color to red
    ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 72, height - 360)

    # Additional Info
    c.setFillColor(colors.black)
    c.drawString(72, height - 500, "Machine concernée :")
    c.setFillColor(colors.red)
    c.drawString(200, height - 500, f"{data['machine_concernee']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 520, "Ou")
    c.setFillColor(colors.red)
    c.drawString(100, height - 520, f"{data['alternative_machines']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 540, "Etat machine :")
    c.setFillColor(colors.red)
    c.drawString(160, height - 540, f"{data['etat_machine']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 560, "Type de machine :")
    c.setFillColor(colors.red)
    c.drawString(180, height - 560, f"{data['type_machine']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 580, "Lieu :")
    c.setFillColor(colors.red)
    c.drawString(120, height - 580, f"{data['lieu']}")

    # Signature Table
    c.setFillColor(colors.black)
    c.drawString(72, height - 620, "Signatures:")
    signature_data = [
        ["Signature Demandeur", "Signature Responsable magasin", "Signature Directeur Général"],
        [f"{data['signature_demandeur']}", "", ""]
    ]
    signature_table = Table(signature_data, colWidths=[2.5*inch, 2.5*inch, 2.5*inch])
    signature_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    signature_table.wrapOn(c, width, height)
    signature_table.drawOn(c, 72, height - 690)

    c.save()
