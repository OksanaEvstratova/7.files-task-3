import os


def sort_by_lines_count(et):
    return et['lines']


result_list = []
file_path = 'files'
files = os.listdir(file_path)
for file_name in files:
    file = os.path.join(file_path, file_name)

    with open(file, encoding='utf-8') as f2:
        data = f2.readlines()
        result_list.append(dict(file_name=file_name, lines=len(data), text_data=data))

result_list.sort(key=sort_by_lines_count)

with open('result.txt', encoding='utf-8', mode='w') as f3:
    for data_file in result_list:
        f3.write(data_file['file_name'] + '\n')
        f3.write(str(data_file['lines']) + '\n')
        for x in data_file['text_data']:
            f3.write(x.strip() + '\n')

with open('result.txt', encoding='utf-8', mode='r') as f4:
    print(f4.read())
