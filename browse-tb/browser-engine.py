import socket
import ssl

# for HTML parshing i suppose 🤔

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

'''///////////////////////////////////////////'''

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

'''///////////////////////////////////////////'''


class URL:

    def __init__(self,url):
        self.schema , url = url.split(":/",1)
        assert self.schema in ["http","https","file","data"]
        url = url[1:]

        if self.schema=="http":
            self.port = 80
        elif self.schema=="https":
            self.port = 443
        
        if self.schema == "file" or self.schema=="data":
            self.path = url
        else:
            if "/"  not in url:
                url += "/"
            self.host , url = url.split("/",1)
            self.path = '/'+ url

            if ":" in self.host:
                self.host , port = self.host.split(":",1)
                self.port = int (port)


        


    def __request__(self):
        
        # data schema implementation

        if self.schema=="data":
            return self.path

        # Making changes to the engine so that it opens the file

        if self.schema == "file":
            file_path = self.path
            
            try:
                file = open(file_path,'r')
            except:
                file = open("./tempFdir/incorrect.txt",'r')
            content = file.read()

            return content

        s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=socket.IPPROTO_TCP,)
        s.connect((self.host,self.port))
        

        if self.schema=="https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s,server_hostname=self.host)

        request = "GET {} HTTP/1.0\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "\r\n";
        s.send(request.encode("utf8"))
        

        response = s.makefile("r",encoding="utf8",newline="\r\n")
        statusline = response.readline()
        version , status, explaination = statusline.split(" ", 2)
        response_headers = {}

        while True:
            line = response.readline()
            if line== "\r\n" : break
            header , value = line.split(":",1)
            response_headers[header.casefold()] = value.strip()
        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers
        content = response.read()
        s.close()
        return content

def show(body):
    in_tag = False
    for c in body:
        if c=='<':
            in_tag = True
        elif c=='>':
            in_tag = False
        elif not in_tag:
            print(c,end="")
def load(url):
    obj = URL(url)
    body = obj.__request__()
    show(body)
            
'''
if __name__ == "__main__":
    import sys
    load(sys.argv[1])
'''

_html = "<tag>This</tag>"
root = htmlTree(_html)


def prRoot(root):
    for c in root.children:
        if isinstance(c, Text):
            print(c.text)
        else:
            print(c.tag)
            prRoot(c)

prRoot(root)

    
