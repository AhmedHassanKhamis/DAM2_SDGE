import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('template.html')

# Render the HTML content by passing dynamic variables
html_content = template.render(title="Sample PDF", heading="Welcome!", content="This is a dynamically generated PDF using wkhtmltopdf and an external CSS.")

# Convert the rendered HTML content to PDF
# Specify the path to the CSS file relative to the HTML file
pdfkit.from_string(html_content, 'output.pdf', css='style.css')

print("PDF successfully created!")
