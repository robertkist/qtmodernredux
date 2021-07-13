[![Build Status](https://www.travis-ci.com/robertkist/qtmodernredux.svg?branch=master)](https://www.travis-ci.com/robertkist/qtmodernredux)

QtModernRedux
=============

Author: Robert Kist (c) 2021 MIT License

QtModernRedux is a modern dark window and widget theme for PySide2, loosely based on and inspired by
Gerard Marull-Paretas' excellent qtmodern 0.2.0 theme (https://pypi.org/project/qtmodern/, MIT License).


Quick-Start
-----------

If you just want to use QtModernRedux, then the quickest way is to install QtModernRedux from PyPi (https://www.pypi.org/project/QtModernRedux/) via pip:

```pip install qtmodernredux```

Screenshots
-----------

Basic Widget on Mac OS:

![QSplitter example](https://user-images.githubusercontent.com/9162068/111871987-e184b500-89c7-11eb-8ec7-be316179a410.png)

Widget collection on Windows:

![widgets example](https://user-images.githubusercontent.com/9162068/111871403-cf554780-89c4-11eb-812b-b78a7366c40d.png)

Custom titlebar on Windows:

![custom titlebar example](https://user-images.githubusercontent.com/9162068/111871399-c8c6d000-89c4-11eb-8266-1b861ef9bedf.png)

Custom titlebar on Mac OS:

![custom titlebar example](https://user-images.githubusercontent.com/9162068/111871747-c6657580-89c6-11eb-8b8c-d19bc550eed0.png)

Features
--------
* Consistent looks across platforms (Mac, Windows, Ubuntu) and monitor DPI settings (regular-DPI, high-DPI/4k, Retina)
* Improved support QDialogs: improved icons, support for QDialog's .exec_() method, support for modal dialogs.
* Provides window scaling controls for 8 cardinal directions.
* Provides a 'no-title bar' mode, allowing users to create modern applications with widgets placed directly into the title-bar
  itself, such as Chrome's "tab titlebar", or MS Teams' titlebar.
* Provides a window drop-shadow for window managers which do not support drow shadows by default on Qt frameless windows.
* Provides vector-based hi-res icons, replacing Qt Fusion style's low quality icons, for some platforms.
* Improved themeing of additional widgets, such as QTableView, QListView, etc.
* Works with tools such as PyInstaller and CxFreeze.
* Provides a work-around for using QMediaPlayer on Windows in styled windows.
* Supports definition of custom styles.

Compatibility
-------------
* Python 3.8 or newer
* PySide2 (tested with 5.15.2)

Tested operating systems:
* MacOS Big Sur (regular DPI and Retina)
* Windows 10 (regular and high-DPI)
* Ubuntu 20.10 (regular and high-DPI)
* PopOS 18.04 (regular and high-DPI)

Building and Installation
-------------------------
Skip this section if you're installing via Pypi.
This section is only relevant if you got QtModernRedux from Github.

This section describes how to create a wheel (.whl) from the code in the repository.
You will need to have Python 3.8 or newer installed in a virtual environment (virtualenv). 
This virtual environment must be located within the root of the qtmodernredux project folder.
You will also need a verion of GNU make. 

* macOS: you can install make via homebrew
* linux: install make via your distribution's package manager
* windows: install make from chocolatey.org (https://chocolatey.org/, https://chocolatey.org/packages/make)

Make sure the virtualenv is active and use pip to install the modules listed in the requirements.txt file.
Then, with the virtualenv active, run ```make wheel```
The wheel (.whl) for your platform can be found in the newly created ```build``` directory.
Use pip to install the wheel that you just built.

Running the Examples
--------------------
Examples can be found at https://github.com/robertkist/qtmodernredux in src/examples.

Before you can run the examples you must install QtModernRedux via pip or build it according to the instructions above.
You will also need to have PySide2 installed, and optionally the ffpyplayer module (see requirements.txt).

Note: if you want to experiment with the examples, you can use ```make examples``` to update the
GUIs for examples - this will re-generate the Python sources from the QDesigner .ui files.

Running the Tests
-----------------
Install the required Python modules from requirements.txt and run ```make tests```.

Usage
-----
Currently, there is no API documentation, but the included examples in the Git repository should provide a 
good starting point for using QtModernRedux.

Notes
-----

* Windows: Windows places the window-controls (minimize, maximize, close) on the right-hand side, whereas macOS puts them on 
  the left-hand side. For Linux, QtModernRedux puts them on the right-hand side by default. This behaviour can be overridden.
* Windows, Linux: on some systems it is not possible to resize a fully maximized window. This is not a bug.
* Windows: dragging a styled window between screens with different scaling factors results in unpredictable behavior and may
  break the theme. This is a limitation of Qt and how Windows handles application scaling. A work-around may be added
  in future versions of QtModernRedux.
* MacOS: Titlebar-less windows may briefly display a title-bar before being minimized. This is a known limitation
  of Qt and not a bug.
* MacOS: Drop shadow: MacOS Big Sur automaticallys add a drop shadow to QtModernRedux windows. Therefore
  the drop-shadow cannot be controlled or customized on these systems. Drop-shadow settings mostly apply to Linux
  window managers.
* All Platforms: Code overriding this style-sheet, e.g. by calling widgets' .setStyleSheet() method, can potentially break the theme.

Limitations
-----------
* Qt offers an extensive widget library with a plethora of customization options. It is well possible that this theme
does not cover all of them. E.g. custom widgets, such as the LCD display widget or the calendar widget, are not covered.
* The goal of this project is not to cover every widget (although it would be nice to eventually achieve this), but 
to cover the most commonly used ones.

Customization
-------------
Have a look at ```src/examples/customstyle``` for an example of a custom style (wow_style).
Styles have 2 parts: styles for the window frame (windowstyle) and the individual widgets (widgetstyle).

Tips:
* do not remove any of the pre-defined constants (see constants.py in windowstyle and widgetstyle directories)
* try to work with the pre-defined constants as much as possible. Many of them are used in qtmodernredux's code
  to enable its functionality.
* some sub-controls of widgets have been disabled (e.g. width set to 0, colors set to transparent, etc.) because they may
  cause problems

Contributions
-------------
Contributions, suggestions and forks are welcome - see https://github.com/robertkist/qtmodernredux
