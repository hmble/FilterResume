import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


original_text = getText('sample.docx')


filter_text = "\n".join([ll.rstrip() for ll in original_text.splitlines() if
                         ll.strip()])


print(filter_text)
print(filter_text.count("Java"))
