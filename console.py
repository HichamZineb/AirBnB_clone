#!/usr/bin/env python3
""" Command interpreter for the AirBnB clone """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = "(hbnb) "
    class_map = {
            "BaseModel": BaseModel, "User": User,
    }

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program using Ctrl-D (EOF) """
        print("")  # Print a new line
        return True

    def emptyline(self):
        """ Do nothing on an empty line """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        Saves it (to the JSON file) and prints the id
        """
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = args.split()
        except ValueError:
            print("** instance id missing **")
            return

        if class_name not in self.class_map:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"

        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Saves the change into the JSON file
        """
        args = args.split()

        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]

            if class_name not in self.class_map:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = f"{class_name}.{obj_id}"

            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception:
            pass

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        try:
            arg_list = args.split()

            if not arg_list:
                instance_list = [str(obj) for obj in storage.all().values()]
            elif arg_list[0] in self.class_map:
                class_name = arg_list[0]
                instance_list = [
                    str(obj) for key, obj in storage.all().items()
                    if class_name in key
                ]
            else:
                print("** class doesn't exist **")

            for instance_str in instance_list:
                print(instance_str)
        except Exception:
            pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        try:
            arg_list = args.split()

            if not arg_list:
                print("** class name missing **")
                return

            class_name = arg_list[0]

            if class_name not in self.class_map:
                print("** class doesn't exist **")
                return

            if len(arg_list) < 2:
                print("** instance id missing **")
                return

            obj_id = arg_list[1]
            key = "{}.{}".format(class_name, obj_id)

            if key not in storage.all():
                print("** no instance found **")
                return

            if len(arg_list) < 3:
                print("** attribute name missing **")
                return

            attr_name = arg_list[2]

            if len(arg_list) < 4:
                print("** value missing **")
                return

            attr_value = arg_list[3]
            instance = storage.all()[key]
            setattr(instance, attr_name, attr_value)
            instance.save()

        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
