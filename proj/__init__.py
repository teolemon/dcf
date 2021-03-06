__version__ = '0.1.1'


def parse_version(version):
    '''
    '0.1.2-dev' -> (0, 1, 2, 'dev')
    '0.1.2' -> (0, 1, 2)
    '''
    v = version.split('.')
    v = v[:-1] + v[-1].split('-')
    ret = []
    for p in v:
        if p.isdigit():
            ret.append(int(p))
        else:
            ret.append(p)
    return tuple(ret)

VERSION = parse_version(__version__)