from pathlib import Path
from drak_archive.file.dvk import Dvk

dvk = Dvk()

file_path = Path("test.dvk").absolute()
print(file_path)
dvk.set_file(file_path)

dvk.set_id("id123")
dvk.set_title("This is a title")
dvk.set_artists(["Artist 2", "Artist 1"])
dvk.set_int_time(2017, 10, 27, 5, 10)
dvk.set_web_tags(["Some", "tags", "here"])
dvk.set_description("This is a description! :)")

dvk.set_page_url("Https://pageurl.com")
dvk.set_direct_url("http://DirectUrl.com")
dvk.set_secondary_url("http://Secondaryurl.COM")

dvk.set_media_file("image.png")
dvk.set_secondary_file("second.tif")
dvk.set_previous_ids(["ran1", "ran2"])
dvk.set_next_ids(["dom1", "dom2"])
dvk.set_section_first(True)
dvk.set_section_last(True)

dvk.set_sequence_title("Seq Title")
dvk.set_section_title("Tis a section")
dvk.set_branch_titles(["Branch 1", "Other"])
dvk.set_rating(4)
dvk.set_views(12)
dvk.set_user_tags(["Yay for tags."])
dvk.write_dvk()