# Filters for files listed in Makefiles

makefilefile = []

def keep_makefilefile(m):
    makefilefile.append(m.group(1))
    return '__KEEPMAKEFILEFILE__' + str(len(makefilefile)) + m.group(2)

def replace_makefilefile(m):
    w = makefilefile[int(m.group(1)) - 1]
    dir_name = os.path.dirname(path)
    
    if dir_name != '/':
        dir_name += '/'

    return '<a href="'+version+'/source'+dir_name+w+'">'+w+'</a>'

makefilefile_filters = {
                'case': 'filename',
                'match': {'Makefile'},
                'prerex': '(?<=\s)(?!/)([-\w/]+/[-\w\.]+)(\s+|$)',
                'prefunc': keep_makefilefile,
                'postrex': '__KEEPMAKEFILEFILE__(\d+)',
                'postfunc': replace_makefilefile
                }

filters.append(makefilefile_filters)
