#!/usr/bin/python3
"""
Unittest for the Console class
Test files by using the following command line:
python3 -m unittest tests/test_console.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("quit  help", output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertRegex(output, r"^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("show User {}".format(obj_id))
                output = f.getvalue().strip()
                self.assertIn("[User]", output)
                self.assertIn(obj_id, output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("destroy User {}".format(obj_id))
                output = f.getvalue().strip()
                self.assertEqual(output, "")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("all")
                output = f.getvalue().strip()
                self.assertIn("[User]", output)
                self.assertIn(obj_id, output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

            self.console.onecmd("update User {} name 'John'".format(obj_id))
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("show User {}".format(obj_id))
                output = f.getvalue().strip()
                self.assertIn("name: 'John'", output)


if __name__ == '__main__':
    unittest.main()

