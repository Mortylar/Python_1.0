import json

def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def flush(source, index):
    res = []
    for i in range(index, len(source)):
        res.append(source[i])
    return res

def sum_json(list1, list2):
    i = 0
    j = 0
    res = []
    while (i < len(list1) and j < len(list2)):
        if (list1[i]['year'] <= list2[j]['year']):
            res.append(list1[i]);
            i += 1
        else: 
            res.append(list2[j]);
            j += 1
        if (i >= len(list1)):
            res.extend(flush(list2, j))
        if (j >= len(list2)):
            res.extend(flush(list1, i))
    return res

def check_keys(source):
    for i in source:
        i['year']
        i['title']

def main():
    try:
        file = read_json('input.txt')
        check_keys(file['list1'])
        check_keys(file['list2'])
        print(json.dumps(sum_json(file['list1'], file['list2']), indent=4))
    except Exception as e:
        print(repr(e))
    

if __name__ == "__main__":
    main();
