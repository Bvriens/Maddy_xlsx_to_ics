import os


class InputHandler:
    @staticmethod
    def get_file_path():
        while True:
            path = input("give path to de directory with the xlsx files (Enter for current dir):")
            if path == "":
                path = "."

            if not os.path.exists(os.path.dirname(path)):
                print("not a valid path try again")
            else:
                return path

    @staticmethod
    def select_filename(filenames):
        for i, filename in enumerate(filenames, 1):
            print(f"{i}. {filename}")

        while True:
            try:
                selected_file_pos = int(input("Enter the number of the file you want process: ").strip())
                selected_filename = filenames[selected_file_pos - 1]

                return selected_filename
            except:  # noqa E722
                print("Not a valid number please try again!")
