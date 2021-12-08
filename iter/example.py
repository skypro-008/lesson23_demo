# with open('./apache_logs_big.txt') as f:
#     file_content = f.read()
#     lines = file_content.split('\n')
#     print(lines[:10])


with open('./apache_logs_big.txt') as f:
    counter = 0
    while True:
        try:
            line = next(f)
        except StopIteration:
            break
        print(line)
        counter += 1
        if counter > 10:
            break


def find(file_path, txt):
    with open(file_path) as f:
        while True:
            try:
                line = next(f)
            except StopIteration:
                break
            if txt in line:
                yield line
