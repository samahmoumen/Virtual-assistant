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
    c.drawCentredString(width / 2, height - 140, "Demande de récupération pièces sur matériel")

    # Personal Info
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(72, height - 180, "Nom demandeur :")
    c.setFillColor(colors.red)
    c.drawString(180, height - 180, f"{data['nom_demandeur']}")
    c.setFillColor(colors.black)
    c.drawRightString(width - 200, height - 180, "Date demande :")
    c.setFillColor(colors.red)
    c.drawRightString(width - 72, height - 180, f"{data['date_demande']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 200, "Type de machine :")
    c.setFillColor(colors.red)
    c.drawString(180, height - 200, f"{data['type_machine']}")
    c.setFillColor(colors.black)
    c.drawString(72, height - 220, "N° de série machine stock :")
    c.setFillColor(colors.red)
    c.drawString(220, height - 220, f"{data['serie_stock']}")
    c.setFillColor(colors.black)
    c.drawString(72, height - 240, "N° Fiche machine :")
    c.setFillColor(colors.red)
    c.drawString(180, height - 240, f"{data['fiche_machine']}")

    # Draw the table of pieces
    table_data = [["Référence Pièce", "Désignation", "QTE"]] + pieces
    table = Table(table_data, colWidths=[2*inch, 3*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 72, height - 320)

    # Additional Info
    c.setFillColor(colors.black)
    c.drawString(72, height - 360, "Pour client :")
    c.setFillColor(colors.red)
    c.drawString(150, height - 360, f"{data['pour_client']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 380, "Etat machine :")
    c.setFillColor(colors.red)
    c.drawString(160, height - 380, f"{data['etat_machine']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 400, "Type de machine client :")
    c.setFillColor(colors.red)
    c.drawString(220, height - 400, f"{data['type_machine_client']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 420, "N° de série machine stock :")
    c.setFillColor(colors.red)
    c.drawString(240, height - 420, f"{data['serie_stock_client']}")

    c.setFillColor(colors.black)
    c.drawString(72, height - 440, "N° Fiche machine :")
    c.setFillColor(colors.red)
    c.drawString(180, height - 440, f"{data['fiche_machine_client']}")

    # Signature Table
    c.setFillColor(colors.black)
    c.drawString(72, height - 480, "Signatures:")
    signature_data = [
        ["Nom et Visa Demandeur", "Visa magasinier", "Visa Directeur Général"],
        [f"{data['visa_demandeur']}", "", ""]
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
    signature_table.drawOn(c, 72, height - 550)

    c.save()
