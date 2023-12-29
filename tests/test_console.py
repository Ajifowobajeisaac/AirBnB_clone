#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.cli = HBNBCommand()

    def test_do_quit(self):
        """Test the do_quit method"""
        self.assertTrue(self.cli.do_quit(''))

    def test_do_EOF(self):
        """Test the do_EOF method"""
        self.assertTrue(self.cli.do_EOF(''))

    def test_emptyline(self):
        """Test the emptyline method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_do_create(self):
        """Test the do_create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue().strip(), "")
            self.assertTrue("BaseModel." + f.getvalue().strip() in storage.all())

    def test_do_show(self):
        """Test the do_show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("show BaseModel " + obj_id)
            self.assertTrue("BaseModel." + obj_id in f.getvalue())

    def test_do_destroy(self):
        """Test the do_destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("destroy BaseModel " + obj_id)
            self.assertFalse("BaseModel." + obj_id in storage.all())

    def test_do_all(self):
        """Test the do_all method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            self.assertTrue("BaseModel." in f.getvalue())

    def test_do_update(self):
        """Test the do_update method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("update BaseModel " + obj_id + " first_name \"John\"")
            self.cli.onecmd("show BaseModel " + obj_id)
            self.assertTrue("'first_name': 'John'" in f.getvalue())

    # Add more test methods here for other methods in HBNBCommand

if __name__ == '__main__':
    unittest.main()
