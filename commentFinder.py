from docx import Document
from lxml import etree
import zipfile
import docx
from docx import *
import pandas as pd
from mainwindow import Ui_MainWindow

class finder:
    def get_document_comments(self, docxFileName):
        self.last_heading = None
        self.df = pd.DataFrame(columns=['comment', 'author', 'date', 'paragraph heading', 'paragraph text'])
        ooXMLns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        comments_dict = {}
        docxZip = zipfile.ZipFile(docxFileName)
        commentsXML = docxZip.read('word/comments.xml')
        et = etree.XML(commentsXML)
        comments = et.xpath('//w:comment', namespaces=ooXMLns)
        for c in comments:
            comment = c.xpath('string(.)', namespaces=ooXMLns)
            comment_id = c.xpath('@w:id', namespaces=ooXMLns)[0]
            comments_dict[comment_id] = comment
            comment_author = c.xpath('@w:author', namespaces=ooXMLns)
            comment_date = c.xpath('@w:date', namespaces=ooXMLns)
            new_row = {'comment' : comment, 'author' : comment_author, 'date' : comment_date, 'paragraph heading' : 1, 'paragraph text': 1}
            if comment != '':
                self.df = self.df.append(new_row, ignore_index=True)
        return comments_dict, self.df

    def paragraph_comments(self, paragraph, comments_dict, document):
        ooXMLns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        comments = []
        if paragraph.style.name.startswith('Heading'):
            self.last_heading = paragraph.text
        for run in paragraph.runs:
            comment_reference = run._r.xpath("./w:commentReference")
            if comment_reference:
                comment_id = comment_reference[0].xpath('@w:id', namespaces=ooXMLns)[0]
                comment = comments_dict[comment_id]
                comments.append(comment)
        return comments, self.last_heading

    def comments_with_reference_paragraph(self, docxFileName, progressBar):
        p_value = 0
        progressBar.setValue(p_value)
        self.main = Ui_MainWindow
        index_val= -1
        document = Document(docxFileName)
        comments_dict, df = self.get_document_comments(docxFileName)
        p_value += 10
        progressBar.setValue(p_value)
        for paragraph in document.paragraphs:
            if comments_dict:
                comments, last_heading= self.paragraph_comments(paragraph, comments_dict, document)
                p_value += 10
                progressBar.setValue(p_value)
                if comments:
                    if p_value < 95:
                        p_value += 5
                        progressBar.setValue(p_value)
                    index_val = index_val+1
                    df.loc[index_val, 'paragraph heading'] = last_heading
                    df.loc[index_val, 'paragraph text'] = paragraph.text

        progressBar.setValue(100)
        return df