from json import load

filename = 'chat.ipynb'

with open(filename) as fp:
    nb = load(fp)
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(line for line in cell['source'] if not line.startswith('%'))
            exec(source, globals(), locals())
