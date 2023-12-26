#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.

The command interpreter handles all the user input and interacts with the
storage and model classes.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for the command interpreter"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place
        }

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

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

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
