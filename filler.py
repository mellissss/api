"""
Файл для тестирования работы сервиса
"""

import requests
from faker import Faker
from prettytable import PrettyTable

API_URL = "http://localhost:8000"

# генерация случайных данных
fake = Faker()


class APIFiller:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_data(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("\nGET request successful!")
            self.display_data(response.json())
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")

    def send_data(self, endpoint: str, payload: dict):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, params=payload)
            response.raise_for_status()
            print("\nPOST request successful!")
            self.display_data([response.json()])
        except requests.RequestException as e:
            print(f"Error during POST request: {e}")

    def delete_data(self, endpoint: str, resource_id: int):
        url = f"{self.base_url}{endpoint}/{resource_id}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            print(f"\nDELETE request successful! Deleted resource with ID {resource_id}")
        except requests.RequestException as e:
            print(f"Error during DELETE request: {e}")

    @staticmethod
    def display_data(data):
        if not data:
            print("No data to display.")
            return
        table = PrettyTable()
        table.field_names = data[0].keys()
        for item in data:
            table.add_row(item.values())
        print(table)


if __name__ == "__main__":
    filler = APIFiller(API_URL)

    print("Adding test authors...")
    for _ in range(3):
        new_author = {"name": fake.name(), "birth_year": fake.random_int(min=1900, max=2023)}
        filler.send_data("/authors/", new_author)

    print("\nFetching all authors...")
    filler.get_data("/authors/")

    print("\nDeleting test authors (IDs 1-3)...")
    for author_id in range(1, 4):
        filler.delete_data("/authors", resource_id=author_id)

    print("\nFetching authors after deletion...")
    filler.get_data("/authors/")
