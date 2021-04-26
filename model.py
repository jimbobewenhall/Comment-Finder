from commentFinder import finder

class Model:
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
        self.find = finder()

    def isValid(self, fileName):
        try:
            file = open(fileName, 'r', errors="ignore")
            file.close()
            return True
        except:
            return False

    def setFileName(self, fileName):
        if self.isValid(fileName):
            self.fileName = fileName
            self.fileContents = open(fileName, 'r', errors="ignore").read()
        else:
            self.fileContents = ""
            self.fileName = ""

    def getFileName(self):
        return self.fileName

    def getFileContents(self):
        return self.fileContents

    def apply(self, progressBar):
        self.comment_dict = self.find.comments_with_reference_paragraph(self.fileName, progressBar)
        return self.comment_dict

    def clear(self):
        pass

    def export(self):
        pass