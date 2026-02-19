
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
            if text.startswith('/'):
                stack.pop()
            else:
                parts = text.split(' ')
                tag_name = parts[0]
                new_el = Element(tag_name, {}, stack[-1])
                stack[-1].children.append(new_el)
                stack.append(new_el)
                in_tag = False
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


