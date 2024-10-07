import pickle
"""Pickling Custom Classes """


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates if the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with name, age, and is_student attributes.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of CustomObject and saves it to a file.

        Parameters:
            filename (str): The name of the file where the object will be
            saved.

        Returns:
            bool: True if serialization is successful, False otherwise.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except (pickle.PicklingError, IOError) as e:
            # You can log the error message e if needed
            return False
        except Exception:
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a file.

        Parameters:
            filename (str): The name of the file from which to load the object.
        Returns:
            CustomObject or None: The deserialized CustomObject instance,
            or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            else:
                return None
        except (pickle.UnpicklingError, IOError) as e:
            # You can log the error message e if needed
            return None
        except Exception:
            return None
