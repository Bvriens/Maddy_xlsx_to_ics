import os


class InputHandler:
    @staticmethod
    def get_file_path():
        while True:
            path = input("give path to de directory with the xlsx files (Enter for current dir):")
            if path == "":
                return "."

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

    @staticmethod
    def select_courses(course_list):
        for i, course in enumerate(course_list, 1):
            print(f"{i}. {course}")

        while True:
            try:
                selected_numbers = input(
                    "Enter the numbers of the courses you want to save, separated by commas: "
                ).split(",")
                selected_numbers = [int(course.strip()) for course in selected_numbers]
                selected_courses = [course_list[i - 1] for i in selected_numbers]

                return selected_courses
            except:  # noqa E722
                print("Not a valid list of numbers please try again!")
