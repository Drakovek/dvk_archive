#!/usr/bin/env python3

from os import mkdir, pardir, remove
from os.path import abspath, basename, exists, join
from dvk_archive.test.temp_dir import get_test_dir
from dvk_archive.main.file.dvk import Dvk
from dvk_archive.main.file.dvk_handler import DvkHandler
from dvk_archive.main.file.dvk_handler import get_directories

def create_test_files() -> str:
    """
    Creates test DVK files to use in unit tests.

    :return: Path of the main test directory
    :rtype: str
    """
    ## CREATE TEST DIRECTORIES
    test_dir = get_test_dir()
    main_sub = abspath(join(test_dir, "sub"))
    mkdir(main_sub)
    empty = abspath(join(test_dir, "empty"))
    mkdir(empty)
    sub_empty = abspath(join(empty, "sub_empty"))
    mkdir(sub_empty)
    empty_2 = abspath(join(test_dir, "empty_2"))
    mkdir(empty_2)
    ## CREATE DVK FILES IN THE MAIN TEMPORARY DIRECTORY
    main_dvk_1 = Dvk()
    main_dvk_1.set_dvk_file(join(test_dir, "main1.dvk"))
    main_dvk_1.set_dvk_id("MAN123")
    main_dvk_1.set_title("Title 10")
    main_dvk_1.set_artist("Artist 1")
    main_dvk_1.set_time_int(2020, 9, 4, 17, 13)
    tags = ["tag1", "other tag", "Tag 3"]
    main_dvk_1.set_web_tags(tags)
    main_dvk_1.set_description("<p>Test &amp; such.</p>")
    main_dvk_1.set_page_url("page/url/")
    main_dvk_1.set_direct_url("/direct/URL/")
    main_dvk_1.set_secondary_url("sec/file/Url")
    main_dvk_1.set_media_file("main.txt")
    main_dvk_1.set_secondary_file("main.jpeg")
    main_dvk_1.write_dvk()
    main_dvk_2 = Dvk()
    main_dvk_2.set_dvk_file(join(test_dir, "main2.dvk"))
    main_dvk_2.set_dvk_id("MAN123")
    main_dvk_2.set_title("TITLE 0.55")
    main_dvk_2.set_artist("Artist 2")
    main_dvk_2.set_page_url("/url/")
    main_dvk_2.set_media_file("main.txt")
    main_dvk_2.set_time_int(2018, 5, 20, 14, 15)
    main_dvk_2.write_dvk()
    ## CREATE DVK FILE IN SUB DIRECTORY
    sub_dvk = Dvk()
    sub_dvk.set_dvk_file(join(main_sub, "sub.dvk"))
    sub_dvk.set_dvk_id("SUB1")
    sub_dvk.set_title("title 0.55")
    sub_dvk.set_artist("Artist 1")
    sub_dvk.set_page_url("/url/")
    sub_dvk.set_media_file("sub.txt")
    sub_dvk.set_time_int(2017, 10, 6, 12, 0)
    sub_dvk.write_dvk()
    ## CREATE DVK FILE IN SUB_EMPTY DIRECTORY
    sub_empty_dvk = Dvk()
    sub_empty_dvk.set_dvk_file(join(sub_empty, "sub_empty.dvk"))
    sub_empty_dvk.set_dvk_id("SBE1")
    sub_empty_dvk.set_title("Title 2")
    sub_empty_dvk.set_artist("Test")
    sub_empty_dvk.set_page_url("/url/")
    sub_empty_dvk.set_media_file("sub.txt")
    sub_empty_dvk.set_time_int(2017, 10, 6, 12, 0)
    sub_empty_dvk.write_dvk()
    ## ASSERT THAT ALL DVKS WERE WRITTEN
    assert exists(main_dvk_1.get_dvk_file())
    assert exists(main_dvk_2.get_dvk_file())
    assert exists(sub_dvk.get_dvk_file())
    assert exists(sub_empty_dvk.get_dvk_file())
    ## RETURN TEST DIRECTORY
    return test_dir

def test_read_dvks():
    """
    Tests the read_dvks method.
    """
    ## TEST LOADING AN INVALID DIRECTORY
    test_dir = create_test_files()
    dvk_handler = DvkHandler()
    assert dvk_handler.get_size() == 0
    dvk_handler.read_dvks(None)
    assert dvk_handler.get_size() == 0
    dvk_handler.read_dvks(join(test_dir, "notreal"))
    assert dvk_handler.get_size() == 0
    ## LOAD DVKS FROM THE MAIN TEST DIRECTORY
    dvk_handler.read_dvks(test_dir)
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 4
    assert dvk_handler.get_dvk(0).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(1).get_title() == "TITLE 0.55"
    assert dvk_handler.get_dvk(2).get_title() == "Title 2"
    assert dvk_handler.get_dvk(3).get_title() == "Title 10"
    ## TEST GETTING ALL INFORMATION FROM DVK
    file = join(dvk_handler.get_dvk(3).get_dvk_file(), pardir)
    assert abspath(file) == test_dir
    file = basename(dvk_handler.get_dvk(3).get_dvk_file())
    assert file == "main1.dvk"
    assert dvk_handler.get_dvk(3).get_dvk_id() == "MAN123"
    assert dvk_handler.get_dvk(3).get_title() == "Title 10"
    assert len(dvk_handler.get_dvk(3).get_artists()) == 1
    assert dvk_handler.get_dvk(3).get_artists()[0] == "Artist 1"
    assert dvk_handler.get_dvk(3).get_time() == "2020/09/04|17:13"
    assert len(dvk_handler.get_dvk(3).get_web_tags()) == 3
    assert dvk_handler.get_dvk(3).get_web_tags()[0] == "tag1"
    assert dvk_handler.get_dvk(3).get_web_tags()[1] == "other tag"
    assert dvk_handler.get_dvk(3).get_web_tags()[2] == "Tag 3"
    assert dvk_handler.get_dvk(3).get_description() == "<p>Test &amp; such.</p>"
    assert dvk_handler.get_dvk(3).get_page_url() == "page/url/"
    assert dvk_handler.get_dvk(3).get_direct_url() == "/direct/URL/"
    assert dvk_handler.get_dvk(3).get_secondary_url() == "sec/file/Url"
    file = join(dvk_handler.get_dvk(3).get_media_file(), pardir)
    assert abspath(file) == test_dir
    file = basename(dvk_handler.get_dvk(3).get_media_file())
    assert file == "main.txt"
    file = join(dvk_handler.get_dvk(3).get_secondary_file(), pardir)
    assert abspath(file) == test_dir
    file = basename(dvk_handler.get_dvk(3).get_secondary_file())
    assert file == "main.jpeg"
    ## TRY READING AN EMPTY DIRECTORY
    empty_2 = abspath(join(test_dir, "empty_2"))
    dvk_handler.read_dvks(empty_2)
    assert dvk_handler.get_size() == 0
    ## TEST READING AFTER NEW DVK HAS BEEN WRITTEN
    new_dvk = Dvk()
    new_dvk.set_dvk_file(join(empty_2, "new_dvk.dvk"))
    new_dvk.set_dvk_id("NEW123")
    new_dvk.set_title("New Dvk")
    new_dvk.set_artist("artist")
    new_dvk.set_page_url("/url/")
    new_dvk.set_media_file("file.png")
    new_dvk.write_dvk()
    assert exists(new_dvk.get_dvk_file())
    dvk_handler.read_dvks(test_dir)
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 5
    assert dvk_handler.get_dvk(0).get_title() == "New Dvk"
    assert dvk_handler.get_dvk(1).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(2).get_title() == "TITLE 0.55"
    assert dvk_handler.get_dvk(3).get_title() == "Title 2"
    assert dvk_handler.get_dvk(4).get_title() == "Title 10"
    ## TEST READING AFTER DVK HAS BEEN MODIFIED
    mod_dvk = dvk_handler.get_dvk(4)
    mod_dvk.set_title("Modified")
    mod_dvk.write_dvk()
    dvk_handler.read_dvks(test_dir)
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 5
    assert dvk_handler.get_dvk(0).get_title() == "Modified"
    assert dvk_handler.get_dvk(1).get_title() == "New Dvk"
    assert dvk_handler.get_dvk(2).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(3).get_title() == "TITLE 0.55"
    assert dvk_handler.get_dvk(4).get_title() == "Title 2"
    ## TEST READING AFTER DVK HAS BEEN DELETED
    remove(dvk_handler.get_dvk(1).get_dvk_file())
    dvk_handler.read_dvks(test_dir)
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 4
    assert dvk_handler.get_dvk(0).get_title() == "Modified"
    assert dvk_handler.get_dvk(1).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(2).get_title() == "TITLE 0.55"
    assert dvk_handler.get_dvk(3).get_title() == "Title 2"

def test_get_directories():
    """
    Tests the get_directories function.
    """
    ## TEST GETTING ALL DIRECTORIES AND SUBDIRECTORIES
    test_dir = create_test_files()
    empty = abspath(join(test_dir, "empty"))
    sub_empty = abspath(join(empty, "sub_empty"))
    empty_2 = abspath(join(test_dir, "empty_2"))
    main_sub = abspath(join(test_dir, "sub"))
    dirs = get_directories(test_dir, False)
    dirs = sorted(dirs)
    assert len(dirs) == 5
    assert dirs[0] == test_dir
    assert dirs[1] == empty
    assert dirs[2] == sub_empty
    assert dirs[3] == empty_2
    assert dirs[4] == main_sub
    ## TEST ONLY GETTING DIRECTORIES WITH DVK FILES
    dirs = get_directories(test_dir, True)
    dirs = sorted(dirs)
    assert len(dirs) == 3
    assert dirs[0] == test_dir
    assert dirs[1] == sub_empty
    assert dirs[2] == main_sub
    ## TEST GETTING DIRECTORIES FROM DIRECTORY WITH NO DVK FILES
    dirs = get_directories(empty_2)
    assert len(dirs) == 0
    ## TEST GETTING INVALID DIRECTORY
    dirs = get_directories(None, False)
    assert len(dirs) == 0
    dirs = get_directories(join(test_dir, "notreal"))
    assert len(dirs) == 0

def test_sort_title():
    """
    Tests the sort_dvks method when sorting alphabetically by title.
    """
    test_dir = create_test_files()
    dvk_handler = DvkHandler(test_dir)
    ## TEST DVKS ARE SORTED BY TITLE
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 4
    assert dvk_handler.get_dvk(0).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(0).get_time() == "2017/10/06|12:00"
    assert dvk_handler.get_dvk(1).get_title() == "TITLE 0.55"
    assert dvk_handler.get_dvk(1).get_time() == "2018/05/20|14:15"
    assert dvk_handler.get_dvk(2).get_title() == "Title 2"
    assert dvk_handler.get_dvk(3).get_title() == "Title 10"
    ## TEST SORTING WITH EMPTY DVK LIST
    dvk_handler.read_dvks(None)
    assert dvk_handler.get_size() == 0
    dvk_handler.sort_dvks("a")
    assert dvk_handler.get_size() == 0

def test_sort_time():
    """
    Tests the sort_dvks method when sorting by publication time.
    """
    test_dir = create_test_files()
    dvk_handler = DvkHandler(test_dir)
    ## TEST DVKS ARE SORTED BY TIME
    dvk_handler.sort_dvks("t")
    assert dvk_handler.get_size() == 4
    assert dvk_handler.get_dvk(0).get_time() == "2017/10/06|12:00"
    assert dvk_handler.get_dvk(0).get_title() == "title 0.55"
    assert dvk_handler.get_dvk(1).get_time() == "2017/10/06|12:00"
    assert dvk_handler.get_dvk(1).get_title() == "Title 2"
    assert dvk_handler.get_dvk(2).get_time() == "2018/05/20|14:15"
    assert dvk_handler.get_dvk(3).get_time() == "2020/09/04|17:13"
    ## TEST SORTING WITH EMPTY DVK LIST
    dvk_handler.read_dvks(None)
    assert dvk_handler.get_size() == 0
    dvk_handler.sort_dvks("t")
    assert dvk_handler.get_size() == 0

def all_tests():
    """
    Runs all tests for the DvkHandler class.
    """
    test_read_dvks()
    test_get_directories()
    test_sort_title()
    test_sort_time()
