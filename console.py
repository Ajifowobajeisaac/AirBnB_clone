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
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Place": Place}
    
    def handle_exception(*args):
        if isinstance(args, KeyError):
            print(f"Error: '{args}' is not a valid class name")
        elif isinstance(args, AttributeError):
            print(f"Error: '{args}' attribute does not exist")
        else:
            print(f"Unexpected error: {args}")

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
         prints the id"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                new_instance = self.classes[args[0]](*args[1:])
                new_instance.save()
                print(new_instance.id)
        except Exception as e:
            self.handle_exception(e)
            
    def do_show(self, args):
        """Prints the string representation of an instance based on the class
         name and id"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.classes:
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
            self.handle_exception(e)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
          into the JSON file)"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.classes:
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
            self.handle_exception(e)

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name"""

        try:
            args = args.split()
            if len(args) > 0 and args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in storage.all().items()
                        if not args or k.split('.')[0] == args[0]])
        except Exception as e:
            self.handle_exception(e)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
          adding or updating attribute (save the change into the JSON file)"""
        try:
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.classes:
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
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
        except Exception as e:
            self.handle_exception(e)

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
