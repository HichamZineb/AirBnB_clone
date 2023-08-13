#!/usr/bin/env python3
""" Command interpreter for the AirBnB clone """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
