import csv
import json
import os
from datetime import datetime


class DataProcessing:
  """Data collection and processing utility class.

  Handles data export to JSON and CSV formats with timestamped filenames.
  """

  def __init__(self, filename: str, data: dict | None = None):
    """Initialize with filename and optional data.

    Args:
        filename (str): Base filename for exported files.
        data (dict, optional): Initial data dictionary. Defaults to None.
    """
    # Date
    now_data = datetime.now().date().strftime("%Y%m%d")
    here = os.path.dirname(__file__)
    home = os.path.abspath(os.path.join(here, "../../../"))
    data = os.path.abspath(os.path.join(home, "data"))

    self.__date = now_data
    self.default_filename = self.__date + "_" + filename

    self.__data = data
    json_dir = os.path.join(self.__data, "json")
    csv_dir = os.path.join(self.__data, "csv")

    self.filepath_json = json_dir
    self.filepath_csv = csv_dir

    self.data = data
    self.number_recorded = 0

  @property
  def data_dict(self) -> dict:
    """Get the current data dictionary.

    Returns:
        dict: The stored data dictionary.
    """
    return self.data

  @data_dict.setter
  def update_data(self, new_data: dict) -> None:
    """Update the data dictionary.

    Args:
        new_data (dict): New data dictionary to store.
    """
    self.data = new_data

  def __is_file_existed(self, filepath: str) -> bool:
    """Check if file already exists.

    Args:
        filepath (str): Path to the file to check.

    Returns:
        bool: True if file exists, False otherwise.
    """
    if os.path.isfile(filepath):
      return True
    else:
      return False

  def write_dict_to_json(self) -> None:
    """Export data dictionary to JSON file.

    Creates a JSON file in the json directory with auto-numbered filename
    if the original filename already exists.
    """
    __filename = os.path.join(self.filepath_json, self.default_filename) + ".json"

    if not self.__is_file_existed(__filename):
      # Write the python dictionary to json file
      with open(__filename, "w") as f:
        json.dump(self.data, f, sort_keys=True, indent=2)
        print("\nThe json file is successfully exported!!!")
    else:
      self.number_recorded += 1
      __next_filename = __filename + str(self.number_recorded)

      with open(__next_filename, "w") as f:
        json.dump(self.data, f, sort_keys=True, indent=2)
        print("\nThe json file is successfully exported!!!")

      # raise Exception("The file is existed, PLEASE change the name")

  def write_dict_to_csv(self, header: list) -> None:
    """Export data dictionary to CSV file.

    Args:
        header (list): List of column headers for the CSV file.

    Raises:
        Exception: If the file already exists.
    """
    __filepath = os.path.join(self.filepath_csv, self.default_filename) + ".csv"
    # Write the python dictionary to csv file
    if not self.__is_file_existed(__filepath):
      with open(__filepath, "w+", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(self.data)
        print("\nThe csv file is successfully exported!!!")
    else:
      raise Exception("The file is existed, PLEASE change the name")
