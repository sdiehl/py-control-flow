import sys

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

filename = None
module = None
code = None

traced = []

def traceit(frame, event, arg):
    if event == "line":
        if module in frame.f_code.co_filename:
            lineno = frame.f_lineno
            #print "line %d: %s" % (lineno, line.rstrip())
            traced.append(lineno)
    return traceit

def draw():
    for index, line in enumerate(traced):
        print line
        if line == 1:
            continue

        lexer = PythonLexer()
        formatter = ImageFormatter(hl_lines=[line], hl_color='#ffaaaa',
                line_pad=0, line_numbers=0, style='colorful')
        contents = highlight(code, lexer, formatter)

        with open('%d.png' % index, 'wa+') as fd:
            fd.write(contents)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        module = filename.split('.')[0]
        code = open(filename).read()

        sys.settrace(traceit)
        __import__(module)
        sys.settrace(None)
        draw()
    else:
        print 'Specify filename of module'
