# from functions.get_file_content import get_file_content

# def test_lorem_truncation():
#     content = get_file_content("calculator", "lorem.txt")

#     # make sure we didn’t get an error
#     assert not content.startswith("Error:")

#     # should be at least 10000 characters
#     assert len(content) >= 10000

#     # should include the truncation message at the end
#     assert 'truncated at 10000 characters' in content

# def test_main_py():
#     content = get_file_content("calculator", "main.py")
#     print(content)

#     assert not content.startswith("Error:")
#     assert "def main" in content

# def test_pkg_calculator_py():
#     content = get_file_content("calculator", "pkg/calculator.py")
#     print(content)

#     assert not content.startswith("Error:")
#     assert "def" in content

# def test_outside_working_dir():
#     content = get_file_content("calculator", "/bin/cat")
#     print(content)

#     assert content.startswith("Error:")

# def test_missing_file():
#     content = get_file_content("calculator", "pkg/does_not_exist.py")
#     print(content)

#     assert content.startswith("Error:")
from functions.get_file_content import get_file_content


def test():
    # long lorem file (truncation behavior)
    result = get_file_content("calculator", "lorem.txt")
    print(result)

    # main.py
    result = get_file_content("calculator", "main.py")
    print(result)

    # pkg/calculator.py
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    # outside working directory
    result = get_file_content("calculator", "/bin/cat")
    print(result)

    # missing file
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    test()