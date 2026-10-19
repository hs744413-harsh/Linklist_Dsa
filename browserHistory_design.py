
class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.current = Node(homepage)

    def visit(self, url):
        new_node = Node(url)

        self.current.next = new_node
        new_node.prev = self.current

        self.current = new_node

    def back(self, steps):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1

        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1

        return self.current.url


# Example
browser = BrowserHistory("google.com")

browser.visit("youtube.com")
browser.visit("github.com")

print(browser.back(1))       # youtube.com
print(browser.back(1))       # google.com
print(browser.forward(2))    # github.com
