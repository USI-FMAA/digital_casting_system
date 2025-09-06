import csv
import json
import os

from .struct import DataObject, DataParam


class DataGathering:
  """Handle data gathering from PLC and export to files.

  Provides functionality for collecting data during PLC operations
  and exporting to JSON and CSV formats.

  Args:
      filename: Base filename for exported data files.
  """

  def __init__(self, filename: str) -> None:
    """Initialize data gathering with specified filename."""
    self._HERE = os.path.dirname(__file__)
    self._HOME = os.path.abspath(os.path.join(self._HERE, "../../../"))
    self._DATA = os.path.abspath(os.path.join(self._HOME, "data"))
    self._JSON_DIR = os.path.join(self._DATA, "json")
    self._CSV_DIR = os.path.join(self._DATA, "csv")
    self.filename = filename

    # Create directories if they don't exist
    os.makedirs(self._JSON_DIR, exist_ok=True)
    os.makedirs(self._CSV_DIR, exist_ok=True)

  def write_dict_to_json(self, data: dict) -> None:
    """Export dictionary data to JSON file.

    Args:
        data: Data dictionary to export to JSON.
    """
    path = os.path.join(self._JSON_DIR, self.filename) + ".json"
    # Write the python dictionary to json file
    with open(path, "w") as f:
      json.dump(data, f, sort_keys=True, indent=5)
      print(f"\nThe json file is sucessfully exported! in {path}")

  def write_dict_to_csv(self, data: list, header: list) -> None:
    """Export list of dictionaries to CSV file.

    Args:
        data: List of dictionaries containing row data.
        header: List of column headers for the CSV file.
    """
    path = os.path.join(self._CSV_DIR, self.filename) + ".csv"
    # Write the python dictionary to csv file
    with open(path, "w+", newline="") as f:
      writer = csv.DictWriter(f, fieldnames=header)
      writer.writeheader()
      writer.writerows(data)
      print(f"\nThe csv file is sucessfully exported! in {self._CSV_DIR}")
