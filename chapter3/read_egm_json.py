import json


def main():
    o = json.load(open('egm.json'))
    items = [node['text'] for node in o['nodes']]
    open('egm.txt', 'w').write('\n'.join(items))


if __name__ == '__main__':
    main()
