# AirBnB clone - The console #
## Description of Project ##
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to * implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
## Command Interpreter for Python ##
A command line interpreter (cmd) for python is a shell that basically performs Read, Evaluate, Print and Loop (REPL) through-out its operation. It allows commands from the user and then executes them The cmd module builds custom shells for a user to work with a program

Below is an example from Python Documentation site
    import cmd, sys
    from turtle import *

    class TurtleShell(cmd.Cmd):
        intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
        prompt = '(turtle) '
        file = None

        # ----- basic turtle commands -----
        def do_forward(self, arg):
            'Move the turtle forward by the specified distance:  FORWARD 10'
            forward(*parse(arg))
        def do_right(self, arg):
            'Turn turtle right by given number of degrees:  RIGHT 20'
            right(*parse(arg))
        def do_left(self, arg):
            'Turn turtle left by given number of degrees:  LEFT 90'
            left(*parse(arg))
        def do_goto(self, arg):
            'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
            goto(*parse(arg))
        def do_home(self, arg):
            'Return turtle to the home position:  HOME'
            home()
        def do_bye(self, arg):
            'Stop recording, close the turtle window, and exit:  BYE'
            print('Thank you for using Turtle')
            self.close()
            bye()
            return True

    if __name__ == '__main__':
        TurtleShell().cmdloop()
