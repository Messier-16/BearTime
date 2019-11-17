class Class():
    classes = []
    def __init__(self, desc, days, times):
        self.desc = desc
        self.days = days
        self.times = times
        Class.classes.append(self)

inp = '''AFRICAM 27AC	Discussion -DIS	
W 4:00P-4:59P
AFRICAM 27AC	Lecture -LEC	
TuTh 2:00P-3:29P
3.0'''
inpfull = '''
AFRICAM 27AC	Discussion -DIS	
W 4:00P-4:59P
AFRICAM 27AC	Lecture -LEC	
TuTh 2:00P-3:29P
3.0
ASTRON C10	Lecture -LEC	
MWF 3:00P-3:59P
4.0
ASTRON C10	Discussion -DIS	
Th 11:00A-11:59A
COMPSCI 61A	Discussion -DIS	
TBA
COMPSCI 61A	Laboratory -LAB	
COMPSCI 61A	Lecture -LEC	
MW 2:00P-2:59P
F 2:00P-2:59P
4.0
COMPSCI 70	Discussion -DIS	
TBA
COMPSCI 70	Lecture -LEC	
TuTh 3:30P-4:59P
4.0
'''
def check_int(s):
    try:
        int(s)
        return True
    except:
        return False

def spacer(lines):
    ret = ''
    for i in range(len(lines)):
        l = lines[i]
        try:
            l1, l2 = lines[i-4], lines[i-1]
        except IndexError:
            l1, l2 = '', ''
        if l == '\n' and (l1 == ':' or l2 == 'A'):
            ret += '\n'
        elif l == '\n':
            ret += ' '
        else:
            ret += l
    return ret

def cleaner(inp):
    removals = ['1.0', '2.0', '3.0', '4.0', '5.0', 'Discussion', 'Lecture', 'Laboratory']
    for s in removals:
        if s in inp:
            inp = inp.replace(s, '')
    return inp

print(spacer(cleaner(inpfull)))

