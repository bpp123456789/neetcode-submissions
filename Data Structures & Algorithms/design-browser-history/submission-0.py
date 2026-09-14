class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.Page(homepage)
        
    class Page:
        def __init__(self, url, back = None, forward = None):
            self.url = url
            self.back = back
            self.forward = forward
        

    def visit(self, url: str) -> None:
        self.head.forward = self.Page(url, self.head)
        self.head = self.head.forward
        return None
        

    def back(self, steps: int) -> str:
        for x in range(0,steps):
            if self.head.back == None:
                return self.head.url
            else:
                self.head = self.head.back
        return self.head.url
        

    def forward(self, steps: int) -> str:
        for x in range(0,steps):
            if self.head.forward == None:
                return self.head.url
            else:
                self.head = self.head.forward
        return self.head.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)