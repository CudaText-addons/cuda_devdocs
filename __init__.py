from cudatext import *
from .proc_word import *
import webbrowser

def do_search(text):
    url = 'http://devdocs.io/#q=' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)
    msg_status('DevDocs: opened browser for "' + text + '"')

class Command:
    def run_input(self):
        text = dlg_input('DevDocs search:', '')
        if text:
            do_search(text)

    def run_text(self):
        if ed.get_sel_mode() == SEL_NORMAL:
            text = ed.get_text_sel()
        else:
            msg_status('DevDocs: only normal selection supported')
            return
        if text:
            do_search(text)
        else:
            x0, y0, nlen, text = get_word_info()
            if text:
                do_search(text)
            else:
                msg_status('DevDocs: need selected text')
