import os
from cudatext import *
from .proc_word import *

def safe_open_url(url):
    '''
    On Windows 10, app crashes when webbrowser.open* is called with running LSP server.
    '''
    if os.name=='nt':
        import subprocess
        subprocess.Popen(['start', url], shell=True)
    else:
        import webbrowser
        webbrowser.open_new_tab(url)


def do_search(text):
    url = 'http://devdocs.io/#q=' + text.replace(' ', '%20')
    safe_open_url(url)
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
