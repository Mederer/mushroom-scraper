import csv


class Mushroom:
    def __init__(self, name, common_name, family, location, dimensions, edibility, description):
        self.name = name
        self.common_name = common_name
        self.family = family
        self.location = location
        self.dimensions = dimensions
        self.edibility = edibility
        self.description = description

    def set_image_urls(self, image_urls):
        self.image_urls = image_urls

    def __str__(self):
        return f"Name: {self.name}\nCommon Name: {self.common_name}\nFamily: {self.family}\nDimensions: {self.dimensions}\nEdibility: {self.edibility}\nDescription: {self.description}"

    @staticmethod
    def write_to_csv(mushrooms):
        filename = "mushrooms.csv"
        with open(filename, "w", newline='', encoding="utf-8") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["Name", "Common Name", "Family",
                               "Dimensions", "Edibility", "Description", "Image"])

            for mushroom in mushrooms:
                csvwriter.writerow([mushroom.name, mushroom.common_name, mushroom.family, mushroom.dimensions,
                                   mushroom.edibility, mushroom.description.replace("\n", "").replace("\r", ""), mushroom.image_urls])
