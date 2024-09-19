from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch

def generate_pdf(data, output_stream, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg'):
    c = canvas.Canvas(output_stream, pagesize=letter)
    width, height = letter

    # Add logo to the PDF
    logo = ImageReader(logo_path)
    c.drawImage(logo, 72, height - 72, width=100, height=50)  # Adjust width/height as needed

    # Date aligned to the right
    c.setFillColor(colors.black)  # Black color for the date
    c.drawRightString(width - 72, height - 72, "Casablanca, le 20/04/2023")

    # Center the title
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)  # Black color for the title
    c.drawCentredString(width / 2, height - 140, "DEMANDE DE DEPART EN CONGE PROFESSIONNEL")

    # Set font for labels and draw them in black
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)  # Black color for labels

    # Draw personal information labels
    c.drawString(72, height - 180, "Nom :")
    c.drawString(width / 3, height - 180, "Prénom :")
    c.drawString(2 * width / 3, height - 180, "Service :")

    c.drawString(72, height - 200, "Fonction :")
    c.drawString(72, height - 220, "Adresse du lieu de congé :")
    c.drawString(72, height - 240, "Téléphone :")

    # Set text color to red for the data values
    c.setFillColor(colors.red)  # Set text color to red

    # Draw the form data in red
    c.drawString(120, height - 180, f"{data['nom']}")
    c.drawString(width / 3 + 60, height - 180, f"{data['prenom']}")
    c.drawString(2 * width / 3 + 60, height - 180, f"{data['service']}")

    c.drawString(150, height - 200, f"{data['fonction']}")
    c.drawString(220, height - 220, f"{data['adresse']}")
    c.drawString(150, height - 240, f"{data['telephone']}")

    # Draw horizontal line
    c.setFillColor(colors.black)  # Back to black for lines
    c.line(72, height - 250, width - 72, height - 250)

    # Table data for "Situation des Droits"
    data_table = [
        ["SITUATION DES DROITS", "NOMBRE DE JOURS"],
        ["Reliquat restant sur la situation", str(data['reliquat'])],
        ["Droit de l’année en cours", str(data['droit_annuel'])],
        ["Total des droits", str(data['total_droits'])]
    ]

    # Create the table with adjusted column widths
    table = Table(data_table, colWidths=[4 * inch, 2 * inch])  # Increase width for both columns
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Draw the table at a specified position
    table.wrapOn(c, width, height)
    table.drawOn(c, 72, height - 350)

    # Draw horizontal line
    c.line(72, height - 390, width - 72, height - 390)

    # Additional details with red text
    c.setFont("Helvetica", 12)# Set text color to black for labels
    c.setFillColor(colors.black)

# Draw labels in black
    c.drawString(72, height - 410, "Motif du congé :")
    c.drawString(72, height - 430, "Date de départ :")
    c.drawString(72, height - 450, "Date de reprise :")
    c.drawString(72, height - 470, "Durée totale prise :")

# Set text color to red for the data values
    c.setFillColor(colors.red)

# Draw the form data in red
    c.drawString(170, height - 410, f"{data['motif']}")
    c.drawString(170, height - 430, f"{data['date_depart']}")
    c.drawString(170, height - 450, f"{data['date_reprise']}")
    c.drawString(180, height - 470, f"{data['duree_totale']} jours")

    # Signatures
    c.setFillColor(colors.black)  # Back to black for signatures
    c.drawString(72, height - 510, "SIGNATURE DE L’AGENT")
    c.drawString(width / 2, height - 510, "SIGNATURE DU RESPONSABLE")

    c.save()
