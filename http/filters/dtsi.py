# Filters for dts includes

dtsi = []

def keep_dtsi(match):
    dtsi.append(match.group(4))
    return match.group(1) + match.group(2) + match.group(3) + '"__KEEPDTSI__' + str(len(dtsi)) + '"'

def replace_dtsi(match):
    w = dtsi[int(match.group(1)) - 1]
    return '<a href="'+version+'/source'+os.path.dirname(path)+'/'+w+'">'+w+'</a>'

dtsi_filters = {
                'case': 'extension',
                'match': {'dts', 'dtsi'},
                'prerex': '^(\s*)(#include|/include/)(\s*)\"(.*?)\"',
                'prefunc': keep_dtsi,
                'postrex': '__KEEPDTSI__(\d+)',
                'postfunc': replace_dtsi
                }

filters.append(dtsi_filters)
