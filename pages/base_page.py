class BasePage:
    'Базовая страница'
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)