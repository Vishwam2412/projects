class Text:
    def __init__(self,text,parent):
        self.text = text
        self.parent = parent
        self.children = []
class Element:
    def __init__(self,tag,attributes,parent):
        self.tag = tag
        self.attributes = attributes
        self.parent = parent
        self.children = []

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []  



'''
class htmlParser:
    def htmlTree(self):
        in_tag = false
        text = ""
        #node = TreeNode()
        stack = []
        for c in page:
            if c=='<':
                in_tag = True
                stack.append(text) 
                text=""
            elif c=='>':
                in_tag = False
                stack.append(text)
                text = ""
            else:
                text += c


        if not in_tag and text:
            self.add_text(text)
'''

voidTags = ["area","base","col","command","embed","hr","img","input","keygen","link","meta","param","source","track","wbr"]

def htmlTree(page):
    
    root = Element("root",{},None)
    stack = [root]
    text = ""

    for c in page:

        if c=='<':
            in_tag = True
            txt = Text(text,stack[-1])
            stack[-1].children.append(txt)
            text=""

        elif c=='>':
            
            if text in voidTags:
                tag = text.split(' ')
                tag_name = tag[0];
                vdTag = Element(tag_name,tag,stack[-1])
                stack[-1].children.append(vdTag)
                #stack.pop()  there is error here as it will pop the parent in which the voidtag are present

            elif text.startswith('/'):
                cmp = stack[-1]

                if text[1:] == cmp.tag:
                    stack.pop()

                else:
                    #here we have a dilemma on what to do include unclosed tag as a text to our file or just ignore it like in modern browser system .
                    #I also thing that adding it as a text may become vulnarable to the code in the future.

                    stack.pop() # It will just pop the topmost shell.
                  # cmp = '<'+cmp+'/>'
                  # parts = cmp.split(' ')
                  # tag_name = parts[0]
                  # new_el = Element(tag_name,{},stack[-1])
                  # stack[-1].children.append(new_el)

            else:
                parts = text.split(' ')
                tag_name = parts[0]
                new_el = Element(tag_name, parts, stack[-1])
                stack[-1].children.append(new_el)
                stack.append(new_el)
                in_tag = false
            text = ""

        else:
            text+=c

    return root

'''
def whitespace(text):
    txt = ""
    for i in len(text):
        if(text[i]!=' '):
            i = i+1
        else:
            
'''


