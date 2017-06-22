import re
from distutils.version import LooseVersion, StrictVersion

def version_compare(old, new):
    def normalize(v):
        response = []
        v = re.sub('[A-Z,a-z]', '', v)
        for x in re.sub(r'(\.0+)*$', '', v).split("."):
            try:
                int(x)
            except:
                continue
            response.append(int(x))
        return response

    is_newer = cmp(normalize(old), normalize(new))

    if is_newer == -1:
        return True
    else:
        return False

OLD = '0.201705011716'
NEW = '0.201705011717.SNAPSHOT'

print(LooseVersion(OLD) < LooseVersion(NEW))