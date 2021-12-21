import pytest
import os
import shutil

dir_path = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/test_dir"
file_path = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/test_file"


@pytest.fixture()
def cr_dir():
    os.mkdir(dir_path)
    return True

@pytest.fixture()
def del_dir():
    os.rmdir(dir_path)
    return True

@pytest.fixture()
def cr_file():
    open(file_path, 'a+')
    return True

@pytest.fixture()
def wr_file():
    try:
        file = open(file_path, "a+")
        file.write("Hello World!")
        file.close()
        return True
    except FileNotFoundError:
        print("Файл не существует")

@pytest.fixture()
def r_file():
    try:
        with open(file_path) as file:
            for line in file:
                print(line)
        return True
    except FileNotFoundError:
        print("Файл не существует")

@pytest.fixture()
def copy_f():
    file_path2 = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/Add_Dir/test_file"
    shutil.copyfile(file_path, file_path2)
    return True

@pytest.fixture()
def name_file():
    try:
        name = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/Add_Dir/test_file_renamed"
        os.rename(file_path, name)
        return True
    except FileNotFoundError:
        print("Файл не существует")

@pytest.fixture()
def move_file():
    try:
        file_path2 = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/Add_Dir/test_file"
        os.replace(file_path2, file_path)
        return True
    except FileNotFoundError:
        print("Файл не существует")

@pytest.fixture()
def del_file():
    file_path2 = "/Users/nikitamozharovskii/Desktop/FINKA/Testing/File_Manager_Testing/Working_Dir/Add_Dir/test_file_renamed"
    os.remove(file_path2)
    return True

def test_cr_dir(cr_dir):
    assert (cr_dir == 1)

def test_del_dir(del_dir):
    assert (del_dir == 1)

def test_cr_file(cr_file):
    assert (cr_file == 1)

def test_wr_file(wr_file):
    assert (wr_file == 1)

def test_copy_f(copy_f):
    assert (copy_f == 1)

def test_name_file(name_file):
    assert (name_file == 1)

def test_move_file(move_file):
    assert (move_file == 1)

def test_del_file(del_file):
    assert (del_file == 1)









