import urwid
import urwid.webutil
import urwid.webdisplay

class Browser:
    def __init__(self):
        self.palette = [
            ('header', 'black', 'light gray', 'standout'),
            ('reveal focus', 'black', 'dark cyan', 'standout'),
            ('status', 'black', 'dark cyan'),
            ('url', 'dark cyan', ''),
            ('highlight', 'light gray', 'dark blue'),
        ]

        self.header = urwid.AttrMap(urwid.Text(" Terminal Web Browser "), 'header')
        self.footer = urwid.AttrMap(urwid.Text(" Press 'Q' to quit "), 'status')
        self.url_edit = urwid.Edit(('url', 'Enter URL: '), wrap='space')

        self.listbox = urwid.ListBox(urwid.SimpleFocusListWalker([self.header, self.url_edit]))

        self.frame = urwid.Frame(
            urwid.AttrMap(urwid.LineBox(self.listbox), 'reveal focus'),
            header=self.header,
            footer=self.footer,
        )

    def main(self):
        self.loop = urwid.MainLoop(
            self.frame,
            self.palette,
            unhandled_input=self.handle_input
        )
        self.loop.run()

    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

if __name__ == '__main__':
    browser = Browser()
    browser.main()
