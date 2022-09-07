#!/usr/bin/python3
'''this module for the console app'''

import cmd
import sys
import shlex
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    '''HBNB Command Prompt class'''

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Executes some actions when the command line is empty.
        Returns:
            bool: Always False.
        """

        return False

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        exit(0)

    def do_EOF(self, arg):
        '''method that handles the EOF and exit the program'''
        # print()
        exit(0)

    def do_create(self, arg):
        ''' creates a new instance of the class passed as argument
            and saves it to the json storage file
        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' prints the string representation of an instance
            based on the class name and id
        '''
        args = shlex.split(arg)

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        all = storage.all()
        if key not in all:
            print("** no instance found **")
            return
        print(all[key])

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id
            and saves the change into the JSON Storage file
        '''
        args = shlex.split(arg)

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        all = storage.all()
        if key not in all:
            print("** no instance found **")
            return

        del (all[key])
        storage.save()

    def do_all(self, arg):
        ''' Prints all string representation of all instances
            based or not on the class name.
        '''
        arg = arg.strip("\"'")
        result = []
        all = storage.all()
        if not arg:
            for key in all.keys():
                result.append(all[key].__str__())
            print(result)
            return

        for key in all.keys():
            if key.find(arg) != -1 and arg in self.classes:
                result.append(all[key].__str__())
        if len(result) <= 0 and arg not in self.classes:
            print("** class doesn't exist **")
            return
        print(result)

    def do_update(self, arg):
        '''  Updates an instance based on the class name
            and id by adding or updating attribute and saves
            the change into the JSON Storage file
        '''
        args = shlex.split(arg)
        cls = id = attr = val = ''

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return
        key = cls + '.' + id
        if key not in storage.all():
            print("** no instance found **")
            return

        arg_section = ''
        if len(args) >= 3:
            arg_section = arg.split(None, 2)[2]
            evaled_args = ''
            try:
                evaled_args = ast.literal_eval(arg_section)
            except (SyntaxError, ValueError, AssertionError):
                pass

            if isinstance(evaled_args, dict):
                arg_section = evaled_args
            else:
                attr = args[2]
        else:
            print("** attribute name missing **")
            return
        if len(args) >= 4:
            if not isinstance(arg_section, dict):
                val = args[3]
        else:
            print("** value missing **")
            return

        obj = storage.all()[key]
        if isinstance(arg_section, dict):
            # type cast the value depends on the attribute
            for key in arg_section.keys():
                if key in self.attr_types:
                    arg_section[key] = self.attr_types[key](arg_section[key])
            # update the object attributes dictionary
            obj.__dict__.update(arg_section)
        else:
            # type cast the value depends on the attribute
            if attr in self.attr_types:
                val = self.attr_types[attr](val)
            new_attr = {attr: val}
            # update the object attributes dictionary
            obj.__dict__.update(new_attr)
        obj.save()

    def do_count(self, args):
        """Counts the number of class instances created"""
        count = 0
        for k in storage.all().keys():
            if args == k.split('.')[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
