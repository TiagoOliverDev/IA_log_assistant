from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(erros, avisos):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Relatório de Erros e Avisos")

    y = height - 80
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Erros:")
    y -= 20

    for erro in erros:
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)
        c.drawString(70, y, f"- {erro}")
        y -= 15

    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Avisos:")
    y -= 20

    for aviso in avisos:
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)
        c.drawString(70, y, f"- {aviso}")
        y -= 15

    c.save()
    buffer.seek(0)
    return buffer
