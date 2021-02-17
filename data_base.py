def load_emails(file_name):
    data = []

    try:
        file = open(file_name, "r") 
        
        for line in file.readlines():
            columns = line.strip().split(",")
            data.append(columns[0])
        file.close()

    except (IndexError, FileNotFoundError):
        pass

    return data

def load_items(file_name):
    data = []

    try:
        file = open(file_name, "r") 

        for line in file.readlines():
            columns = line.strip().split("/")
            item = {
                'name': columns[0],
                'value': int(columns[1]),
                'quantity': int(columns[2]),
            }
            data.append(item)
        file.close()

    except (IndexError, FileNotFoundError):
        pass

    return data