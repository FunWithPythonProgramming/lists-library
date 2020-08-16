# important code that we will eventually need
self.file_name = os_path_join(os_path_expanduser("~"), ".list_manager")
if not os_path_exists(self.file_name):
    self.lists = {}
else:
    with open(self.file_name, "r") as json_input_file:
        json_output = json_load(json_input_file)
        self.lists = json_output.get("lists")