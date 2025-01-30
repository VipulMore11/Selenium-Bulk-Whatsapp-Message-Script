def clean_file(file):
	file = open(file,"r+")

	file.truncate(0)
	
	file.close()

def read_file(file, array=False):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read()

    if array:
        lines = lines.split('\n')

    return lines


def write_file(file, message):
	f = open(file, "a")
	f.write(f"{message}\n")

	f.close()

	return "Success"