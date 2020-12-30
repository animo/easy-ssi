import os

from proposals import root_folder, walk, status_list


def update(fname, tmp_fname):
    if not os.path.exists(fname):
        os.rename(tmp_fname, fname)
        print('Generated %s.' % fname)
        return
    with open(fname, encoding='utf-8', mode='rt') as f:
        old = f.read()
    with open(tmp_fname, encoding='utf-8', mode='rt') as f:
        new = f.read()
    if old == new:
        print('No change to %s.' % fname)
        os.remove(tmp_fname)
        return
    os.remove(fname)
    os.rename(tmp_fname, fname)
    print('Updated %s.' % fname)


def main(name, dir, fname):
    fname = os.path.join(root_folder, fname)
    # Load all metadata
    all = [proposal for proposal in walk(dir)]
    tmp_fname = fname + '.tmp'
    with open(fname, 'r', encoding='utf-8') as curr, open(tmp_fname, 'w', encoding='utf-8') as out:
        current = curr.read()
        parts = current.split(f'## {name} Overview')
        prefix = parts[0]
        out.write(prefix)
        out.write(f"## {name} Overview\n")
        for status in status_list:
            out.write(f"\n### {status}\n")
            with_status = [proposal for proposal in all if proposal.status == status]
            for proposal in with_status:
                line = f"* [{proposal.title}]({proposal.relpath})"
                out.write(line + '\n')
        out.write("\n\n>(This file is machine-generated; see [code/generate_index.py](code/generate_index.py).)\n")
    update(fname, tmp_fname)


if __name__ == '__main__':
    main('Plugins', 'plugins', 'plugins.md')
    main('Presets', 'presets', 'presets.md')
