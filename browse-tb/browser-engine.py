import socket 
import ssl
import tkinter
import tkinter.font

#bi_times = tkinter.font.Font(
#    family="Times",
#    size=16,
#    weight="bold",
#    slant="italic",
#)


WIDTH , HEIGHT = 800 , 900
SCROLL_STEP = 100
HSTEP , VSTEP = 13,18
class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
                self.window,
                width = WIDTH,
                height = HEIGHT
            )
        self.canvas.pack()
        self.scroll = 0
        self.display_list = []
        self.window.bind("<Down>",self.scrolldown)
        self.window.bind("<Up>",self.scrollup)
        #self.window.bind("<MouseWheel",self.mouse_wheel_action)
        self.window.bind("<Button-4>",self.scrollup)
        self.window.bind("<Button-5>",self.scrolldown)

    
    """"

    def mouse_wheel_action(event):
        if event.delta>0:
            self.scrollup
        else:
            self.scrolldown

    """


    def scrolldown(self,e):
        self.scroll += SCROLL_STEP
        self.draw(self.display_list)

    def scrollup(self,e):
        if self.scroll == 0 :
            return
        self.scroll -= SCROLL_STEP
        self.draw(self.display_list)
    
    def load(self,url):
        obj = URL(url)
        body = obj.__request__()
        te = lex(body)
        display_list = layout(te)
        self.draw(display_list);

    
    def draw(self, display_list):
        self.canvas.delete("all")
        for x , y , ch in display_list:
            if y>self.scroll + HEIGHT:continue
            if y+VSTEP < self.scroll :continue
            self.display_list = display_list
            self.canvas.create_text(x,y-self.scroll,text=ch )

        
        '''
        self.canvas.create_rectangle(10,20,400,300)
        self.canvas.create_oval(100,100,150,150)

        self.canvas.create_text(200,150,text=te)
        HSTEP, VSTEP = 13,18
        x_co , y_co = HSTEP , VSTEP
        for c in te:
            self.canvas.create_text(x_co,y_co,text=c)
            x_co += HSTEP;
            if x_co > WEDTH-HSTEP:
                y_co += VSTEP
                x_co = HSTEP
            elif y_co>HEIGHT-VSTEP:
                break
        '''

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


#def layout(text):
#    display_list = []
#    HSTEP , VSTEP = 13,18
#    cursor_x , cursor_y = HSTEP , VSTEP
#    for c in text:
#        display_list.append((cursor_x,cursor_y,c))
#        cursor_x += HSTEP
#        if(c=='\n' or cursor_x >= WIDTH-HSTEP):
#            cursor_y += VSTEP
#            cursor_x = HSTEP
#    return display_list

def layout(text):
    font = tkinter.font.Font()
    display_list = []
    HSTEP , VSTEP = 13 , 18
    cursor_x , cursor_y = HSTEP , VSTEP
    for word in text.split():
        w = font.measure(word)
        if cursor_x+w>WIDTH-HSTEP:
            cursor_y += font.metrics("linespace") *1.25
            cursor_x = HSTEP
        display_list.append((cursor_x,cursor_y,word))
        cursor_x += w + font.measure(" ")
    return display_list




def lex(body):
    in_tag = False;
    text = ""
    for c in body:
        if c=='<':
            in_tag = True
        elif c=='>':
            in_tag = False
        elif not in_tag:
            text += c
    return text


def mouse_wheel_action(event):
    if event.delta>0:
        self


'''
def load(url):
    obj = URL(url)
    body = obj.__request__()
    show(body)
            

if __name__ == "__main__":
    import sys
    load(sys.argv[1])


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
'''

if __name__ == "__main__":
    import sys
    browser = Browser()
    browser.load(sys.argv[1])
    tkinter.mainloop()


  
