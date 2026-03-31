import json

def json_diff(a, b, path=''):
    diffs = []

    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()).union(b.keys())
        for key in keys:
            new_path = f"{path}.{key}" if path else key
            if key not in a:
                diffs.append((new_path, None, b[key]))
            elif key not in b:
                diffs.append((new_path, a[key], None))
            else:
                diffs.extend(json_diff(a[key], b[key], new_path))

    elif isinstance(a, list) and isinstance(b, list):
        max_len = max(len(a), len(b))
        for i in range(max_len):
            new_path = f"{path}[{i}]"
            if i >= len(a):
                diffs.append((new_path, None, b[i]))
            elif i >= len(b):
                diffs.append((new_path, a[i], None))
            else:
                diffs.extend(json_diff(a[i], b[i], new_path))

    else:
        if a != b:
            diffs.append((path, a, b))

    return diffs

if __name__ == "__main__":
    with open("file1.json", "r") as f:
        json1 = json.load(f)
    with open("file2.json", "r") as f:
        json2 = json.load(f)

    differences = json_diff(json1, json2)

    for diff in differences:
        print(diff)
