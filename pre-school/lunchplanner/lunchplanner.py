"""
Planning a week or multiple weeks of lunch and writes to printable txt-file,
future improvement supposal: stock inventory of ingredients to remind grocery shopping
"""
import random

FOOD_LIST = [
    "Taco-pirog", "Pizza-bullar", "Frukt", "Nudlar",
    "Köttbulle-smörgås", "placeholder 1", "placeholder 2"
]
WEEKDAYS = [
    "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"
]

class LunchMenu:
    """
    takes a list of food and number of weeks
    """
    def __init__(self, food_list, weeks=1) -> None:
        self.food_list: list = food_list
        self.weeks:int = weeks
        self.all_weeks: list = []

    def generate_random_week(self) -> list:
        """
        generates a shuffled list of food_list
        :return
        str: with random shuffled list of food_list
        """
        return random.sample(self.food_list, len(self.food_list))

    def generate(self) -> list:
        """
        generates a dictionary with week(s) and menu(s) which is stored and returned in a list
        :return
        list: dictionary with weeknumber and weekmenu
        """
        self.all_weeks = []

        for week in range(1, self.weeks + 1):
            week_data: dict = {
                "title": f"Vecka {week}",
                "menu": self.generate_random_week()
            }
            self.all_weeks.append(week_data)

        return self.all_weeks

    def __str__(self) -> str:
        output: list = []

        for week in self.all_weeks:
            output.append(week["title"])
            output.append("-" * 20)

            for day, food in zip(WEEKDAYS, week["menu"]):
                output.append(f"{day.ljust(10)}:\t{food}")
            output.append("")

        return "\n".join(output)

    def save_to_file(self, filename=None):
        """
        saves list of week(s) with menu(s) to file on my own desktop as default,
        default WILL NOT WORK FOR OTHER USERS so add argument in main function if needed
        :param filename: shortcut to savefile
        """
        if filename is None:
            filename = r"C:\Users\fdasfda\Desktop\veckomeny.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self))


def main() -> None:
    """
    runs main function
    """
    weeks: int = int(input("Hur många veckor vill du planera? "))

    planner = LunchMenu(FOOD_LIST, weeks)
    planner.generate()

    print(planner)
    planner.save_to_file()



if __name__ == "__main__":
    main()
