import socket
import ssl


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
            

if __name__ == "__main__":
    import sys
    load(sys.argv[1])

