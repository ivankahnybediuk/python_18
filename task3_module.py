def linesCounter(file):
    text = open(file).readlines()
    return len(text)

def charsCounter(file):
    text = open(file).read()
    return len(text)