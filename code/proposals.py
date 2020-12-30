import collections
import os
import re

Proposal = collections.namedtuple('Proposal', 'title abspath relpath status')


status_list = ["Implemented", "Work In Progress", "Accepted", "Proposed"]


root_folder = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

def walk_files(dir: str):
    """
    Generate the full path to every proposal in the directory.
    """
    for root, folders, files in os.walk(os.path.join(root_folder, dir), topdown=True):
        for f in files:
            if not f.startswith('.'):
                proposal_path = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
                yield proposal_path
        # Don't recurse
        folders.clear()
        files.clear()


_field = lambda x: re.compile(r'^[ \t]*[-*][ \t]*' + x + '[ \t]*:[ \t*](.*?)$', re.I | re.M)
_title_pat = re.compile(r'\s*#[ \t]*(?:Preset |Plugin )[ \t]*-[ \t]*(.*?)$', re.I | re.M)
_status_pat = _field('Status')
_status_val_pat = re.compile(r'\[[ \t]*(\w+)')

def walk(dir: str):
    """
    Generate a proposal tuple for every proposal in a specific directory.
    """
    for abspath in walk_files(dir):
        with open(abspath, 'rt', encoding='utf-8') as f:
            txt = f.read()
        m = _title_pat.search(txt)
        if m:
            title = m.group(1)
        else:
            title = '', ''
        rpath = relpath(abspath)
        status = _status_pat.search(txt).group(1)
        m = _status_val_pat.search(status)
        if m:
            status = m.group(1)
        x = Proposal(title, abspath, rpath, status)
        yield x


def relpath(abspath):
    return os.path.relpath(abspath, root_folder).replace('\\', '/')


_header_pat = re.compile(r'^\s*#+[ \t]*(.*?)$', re.M)

def walk_headers(txt):
    """
    Generate a regex match object for each markdown header in a doc. This matcher
    can be used to find the header or to extract the text of the header.
    """
    for match in _header_pat.finditer(txt):
        yield match


_link_split_pat = re.compile(r'\[(.*?)\]\((.*?)\).*', re.DOTALL)
def split_hyperlink(txt):
    """
    Turn a markdown hyperlink [...](...) into a (clickable_text, uri) pair.
    """
    m = _link_split_pat.match(txt)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return None, None