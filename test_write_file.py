from functions.write_file import write_file

def test():
    # normal write
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    # write to a new file in a subdirectory
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    # attempt to write to a directory
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()