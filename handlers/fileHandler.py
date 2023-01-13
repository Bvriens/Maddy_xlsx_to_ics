import os
from .inputHandler import InputHandler


class FileHandler:
    def __init__(self) -> None:
        self.selected_filename = None
        self.path = None

    def find_all_xlsx_files(self, path=".") -> list[str]:
        files = [f for f in os.listdir(path) if f.endswith(".xlsx")]
        return files

    def select_file(self) -> str:
        while True:
            self.path = InputHandler.get_file_path()
            list_of_xlsx = self.find_all_xlsx_files(path=self.path)

            if len(list_of_xlsx) < 1:
                print("No .xlsx files found! Please tye again!")
            else:
                self.selected_filename = InputHandler.select_filename(list_of_xlsx)
                return self.path + "\\" + self.selected_filename


if __name__ == "__main__":
    filehandler = FileHandler()
    print(filehandler.select_file())
