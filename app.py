import sys
import os
from workers import XmlWorker, SystemWorker

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'ERROR: No repo directory passed.'
        sys.exit(1)
    else:
        rpm_dir = sys.argv[1]

    if not os.path.isdir(os.path.join(rpm_dir, 'repodata')):
        print("ERROR: No 'repodata' directory found.")

    full_file_path = os.path.join(rpm_dir, 'repodata', 'repomd.xml')
    XmlWorker.parse_repomd_xml(full_file_path)

    # for file in os.listdir(os.path.join(rpm_dir, 'repodata')):
    #     full_file_path = os.path.join(rpm_dir, 'repodata', file)
    #     if file.endswith('.xml.gz'):
    #         XmlWorker.parse_tree(full_file_path)
