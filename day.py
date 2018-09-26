from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import Flowable
from reportlab.pdfbase.ttfonts import TTFont

import os
import sys
import datetime

def tag_visible(element):
    # Filter function to get all visible elements
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def text_from_html(body):
    # Scrape all visible text from a url
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u"<br />".join(t.strip() for t in visible_texts)

def text_to_pdf(content):
    # Create a buffer file, set-up title and file name
    date = datetime.datetime.now()
    my_doc = SimpleDocTemplate("Day-nytimes-" + str(date.strftime("%Y%m%d")) + '.pdf')
    title = 'DAY - nytimes.com ' + date.strftime("%x")
    my_doc.title = title

    # Set the styles for the title and body
    sample_style_sheet = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('Times_New_Roman',
    get_script_path() + "/font/Times_New_Roman.ttf"))

    title_style = sample_style_sheet['Heading1']
    title_style.fontName = 'Times_New_Roman'
    title_style.fontSize = 24

    body_style = sample_style_sheet['BodyText']
    body_style.fontName = 'Times_New_Roman'
    body_style.fontSize = 12

    # Collect content and write to PDF
    flowables = []
    title_text = Paragraph(title, sample_style_sheet['Heading1'])
    body_text = Paragraph(content, sample_style_sheet['BodyText'])
    flowables += [title_text, body_text]
    my_doc.build(flowables)

    return True

html = urllib.request.urlopen('http://www.nytimes.com').read()
print(text_from_html(html))
text_to_pdf(text_from_html(html))