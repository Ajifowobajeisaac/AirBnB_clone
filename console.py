#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.

The command interpreter handles all the user input and interacts with the
storage and model classes.
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for the command interpreter"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review,
        }

    def do_count(self, args):
        """Retrieves the number of instances of a class"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                print(len([v for k, v in storage.all().items() if
                           k.split('.')[0] == args[0]]))
        except Exception as e:
            pass

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name"""

        try:
            args = args.split()
            if len(args) > 0 and args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                print(
                    [str(v) for k, v in storage.all().items() if not
                        args or k.split('.')[0] == args[0]]
                    )
        except Exception as e:
            pass

    def default(self, line):
        """
        Method called on an input line when the command prefix is not
        recognized
        """

        match = re.search(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            args = match.group(3)
            if class_name in self.__classes:
                if method_name == "all":
                    self.do_all(class_name)
                elif method_name == "count":
                    self.do_count(class_name)
                elif method_name == "show":
                    self.do_show(class_name + " " + args)
                elif method_name == "destroy":
                    self.do_destroy(class_name + " " + args)
                elif method_name == "update":
                     # Use regex to match either a sequence of non-space 
                     # characters or a sequence of characters within
                     # double quotes
                    args = re.findall(r'[^,\s]+|"[^"]*"', args)
                    # Remove quotes from arguments
                    args = [arg.replace('"', '') for arg in args]
                    # Call do_update with the correctly parsed arguments
                    if len(args) == 3:
                        self.do_update(
                            f"{class_name} {args[0]} {args[1]} {args[2]}")
                    elif len(args) == 2:
                    # Check if the second argument is a dictionary
                        try:
                            attributes = eval(args[1])
                            if isinstance(attributes, dict):
                                for key, value in attributes.items():
                                    self.do_update(
                                        f"{class_name} {args[0]} {key} {value}"
                                        )
                            else:
                                print("** attribute must be a dictionary **")
                        except:
                            print("** value mustbe a dictionary **")
                    else:
                        print("** invalid number of arguments **")

        if line.endswith(".all()"):
            class_name = line.split(".")[0]
            if class_name in self.__classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif line.endswith(".count()"):
            class_name = line.split(".")[0]
            if class_name in self.__classes:
                self.do_count(class_name)
            else:
                print("** class doesn't exist **")
        elif line.endswith("show(<id>)"):
            class_name = line.split("(")[0]
            if class_name in self.__classes:
                self.do_show(class_name + " " + line.split('"')[1])
            else:
                print("** class doesn't exist **")
        elif line.endswith("destroy(<id>)"):
            class_name = line.split("(")[0]
            if class_name in self.__classes:
                self.do_destroy(class_name + " " + line.split('"')[1])
            else:
                print("** class doesn't exist **")
        elif line.endswith("update(<id>, <attribute name>, <attribute value>)"):
            class_name = line.split("(")[0]
            if class_name in self.__classes:
                args = line.split('"')
                self.do_update(class_name + " " + args[1] + ", " + args[3] +
                               ", " + args[5])
            else:
                print("** class doesn't exist **")
        elif line.endswith("update(<id>, <dictionary representation>)"):
            class_name = line.split("(")[0]
            if class_name in self.__classes:
                args = line.split('"')
                self.do_update(class_name + " " + args[1] + ", " + args[3])
            else:
                print("** class doesn't exist **")

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
         prints the id"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                new_instance = self.__classes[args[0]]()
                new_instance.save()
                print(new_instance.id)
        except Exception as e:
            pass

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
         name and id"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
        except Exception as e:
            pass

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
          into the JSON file)"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
        except Exception as e:
            pass

    def do_update(self, args):
        """Updates an instance based on the class name and id by
          adding or updating attribute (save the change into the JSON file)"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    if args[2] in ['id', 'created_at', 'updated_at']:
                        print("** attribute can't be updated **")
                    else:
                        try:
                            attributes = eval(args[2])
                            if isinstance(attributes, dict):
                                for attr_name, attr_value in attributes.items():
                                    attr_type = type(getattr(storage.all()[key], attr_name, ""))
                                    if attr_type in [int, float, str]:
                                        setattr(storage.all()[key], attr_name, attr_type(attr_value))
                                        storage.all()[key].save()
                                    else:
                                        print("** attribute type not allowed **")
                            else:
                                print("** value must be a dictionary **")
                        except:
                            print("** value must be a dictionary **")
        except Exception as e:
            pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
