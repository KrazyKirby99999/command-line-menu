Command Line Menu
===============================================

2020-10-22

* [Prerelease v0.2](https://github.com/KrazyKirby99999/command-line-menu/releases/tag/0.2)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)

Installation
------------
* Prerequisites
    - Python 3.4 or higher

* Have Python 3.4 or higher installed with pip
  Install Python from [HERE](https://www.python.org/) if not already installed.

* Install the latest release of the package from pip
        python -m pip install --upgrade pip
		pip install Command-Line-Menu==0.2.2

Usage
------------
* Import module
        from command_line_menu import menu

* Create object from the class NewMenu 
        mymenu = menu.NewMenu()

* Add title to menu
        mymenu.set_title("Example New Title")

* Add command option to menu
        mymenu.add_command("Do the command that prints \\"Hello World\\"",print,"Hello World")

* Display menu and loop
        mymenu.loop()

* Display menu once (optional, can be used instead of the method .loop() )
        mymenu.show()

Features
------------
* Complete
    - Add title to menu	(v0.1-)
	- Add options to menu (v0.1-)
	- Add number list to choose menu options (v0.1)
	- Add ability to loop to menu (v0.2)

* In Progress
	- Add description to menu
    - Add option to hide console output from menu options
	- Improve "Add options to menu"

* Planned
	- Add support for sub-menus to menu options
    - Add alphabet to choose menu options
	- Add custom list to choose menu options
	- Add error handling


Bug reports and feature requests
--------------------------------
Please submit tickets on the [issues](https://github.com/KrazyKirby99999/command-line-menu/issues) page.

