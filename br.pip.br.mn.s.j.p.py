import w3m

class TerminalBrowser:
    def __init__(self):
        self.browser = w3m.W3m()

    def load_url(self, url):
        self.browser.load(url)

    def main(self):
        while True:
            user_input = input("Enter URL (type 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            self.load_url(user_input)
            self.display_page()

    def display_page(self):
        page_content = self.browser.document()
        print(page_content)

if __name__ == '__main__':
    browser = TerminalBrowser()
    browser.main()
