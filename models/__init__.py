#!/usr/bin/python3
"""
This module initializes the FileStorage instance for your application.

The FileStorage instance is responsible for the serialization and
deserialization of all your data, following the FileStorage class definition
from the `models/engine/file_storage.py` file.
"""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Load serialized data from the file system, if any.
storage.reload()
