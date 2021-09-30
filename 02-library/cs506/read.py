def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open("example.txt", "r") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
        return words
