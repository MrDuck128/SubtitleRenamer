import os, sys

if len(sys.argv) > 1:
    path = ' '.join(sys.argv[1:])

    if not os.path.isdir(path):
        input('Enter a valid path.\nPress enter to exit...')
        exit(0)

else:
    path = os.getcwd()

subName = 0
for file in os.listdir(path):
    if file[-4:] == '.srt' and file[-8:-4] != '-eng':
        subName = file
        break

if subName:
    with open(os.path.join(path, subName)) as f:
        sub = f.read()

    sub = sub.replace('ð', 'đ').replace('æ', 'ć').replace('è', 'č').replace('Æ', 'Ć').replace('È', 'Č')

    with open(os.path.join(path, subName), 'w', encoding='utf-8') as f:
        f.write(sub)

    input('Success.\nPress any key to exit...')

else:
    input('No subtitle files available.\nPress any key to exit...')