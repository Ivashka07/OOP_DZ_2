files = ["text_1.txt", "text_2.txt", "text_3.txt"]

files_content = []

def read_file_name(file): 
    file_name = {}
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        file_name[file] = {
            "count": len(lines),
            "lines": ", ".join(lines),
        }
        files_content.append(file_name)

def sort_files(files):
    n = len(files)
    for i in range(n):
        for j in range(0, n-i-1):
            if files[j][list(files[j].keys())[0]]["count"] > files[j+1][list(files[j+1].keys())[0]]["count"]:
                files[i], files[j+1] = files[j+1], files[i]
    return files

def write_in_file(files):
    with open("result.txt", "w", encoding="utf-8") as f:
        for file in files:
            key = list(file.keys())[0]
            content = file[key]
            f.write(f"{key}\n{content['count']}\n{content['lines']}\n")

for file in files:
    read_file_name(file)

files_content = sort_files(files_content)

write_in_file(files_content)

