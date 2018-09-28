# Programmatic Day

In his book [Uncreative Writing]([http://cup.columbia.edu/book/uncreative-writing/9780231149907),](http://cup.columbia.edu/book/uncreative-writing/9780231149907),) Kenneth Goldsmith explores where the lines between authorship and appropriation lie in the age of digital media. [Day]([https://www.goodreads.com/book/show/764260.Day)](https://www.goodreads.com/book/show/764260.Day)) is one of his examples of uncreative writing: It is a poem featuring all text published in the New York Times of september 1, 2000. From op-ed to advertisement, everything is set in Times New Roman 12pt.

>  'I began retyping the day's New York Times, word for word, letter for letter, from the upper left hand corner to the lower right hand corner, page by page.'

Programmatic Day is a small python script to create your own version of Day, based on the homepage of nytimes.com. After running the script you get a PDF with all text of the digital frontpage of today.

![Example of a frontpage]([https://pzwiki.wdka.nl/mw-mediadesign/images/9/98/Day_02.png](https://pzwiki.wdka.nl/mw-mediadesign/images/9/98/Day_02.png))

## Getting Started

Clone the repository and run the script. The PDF will be saved in the same directory.

### Prerequisites

The script is written for Python 3. To install the required libraries run 'pip3 install -r requirements.txt'

## Acknowledgments

This script is one of the experiments I did to learn about webscraping using Python, and using the material in derivative work. I'd like to thank the following people for their examples:

* Ryan Newton, for [his post]([https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef)](https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef)) on generating pdf's with ReportLab
* Code examples for [the snippet]([https://code-examples.net/en/q/1d8c52)](https://code-examples.net/en/q/1d8c52)) to let Beautifulsoup only fetch visible elements