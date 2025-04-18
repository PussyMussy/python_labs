col_index = 4

def get_mean_size(ls_output):
    total_size = 0
    file_count = 0

    for line in ls_output.strip().split('\n'):
        columns = line.split()

        if len(columns) < col_index:
            continue

        try:
            total_size += int(columns[col_index])
            file_count += 1
        except (ValueError, IndexError):
            continue

    if file_count == 0:
        return None
    
    return total_size / file_count

if __name__ == '__main__':
    import sys

    ls_output = sys.stdin.read()
    mean_size = get_mean_size(ls_output)

    if mean_size is None:
        print("Нет данных для обработки")
    else:
        print(f"Average: {mean_size:.2f} bytes")