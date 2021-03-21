UIC := pyside2-uic
RCC := pyside2-rcc
ECHO := echo
CAT := cat
RM := rm
PIP := pip3
PYTHON := python3
RESOURCES_OS := resources_nix

ifdef OS  # Windows: only Windows has the OS environment variable defined
	PIP := pip
	PYTHON := python
	RM := del
	CAT := type
	RESOURCES_OS := resources_win
endif

# Runs mypy test on a specific file or directory
define run_mypy
	$(ECHO) "mypy checking $(1)"
	mypy \
	--disallow-any-generics \
	--ignore-missing-imports \
	--no-incremental \
	--strict-equality \
	--disallow-incomplete-defs \
	--disallow-redefinition \
	--disallow-untyped-globals \
	--no-implicit-optional \
	--no-implicit-reexport \
	--warn-redundant-casts \
	--warn-unused-ignores \
	--warn-unreachable \
	--warn-no-return \
	--disallow-untyped-calls \
	--disallow-untyped-defs \
	--check-untyped-defs \
	--disallow-any-generics \
	--warn-return-any \
	$(1)
endef

# Runs flake8 test on a specific file or directory
define run_flake8
	$(ECHO) "flake8 checking $(1)"
	flake8 \
	--ignore E501,F401,F403,C901,W504,E722,E129,E126 \
	--format=pylint \
	$(1)
endef

# Runs pylint test on a specific file or directory
define run_pylint
	$(ECHO) "pylint checking $(1)"
	pylint \
	--reports=n \
	--score=n \
	--ignore-patterns=.*_ui.py \
	--extension-pkg-whitelist=PySide2,shiboken2 \
	--msg-template="{path}:{module}:{line}: [{msg_id}({symbol}), {obj}] {msg}"\
	--jobs=0 \
	-d attribute-defined-outside-init \
	-d global-statement \
	-d unsubscriptable-object \
	-d consider-iterating-dictionary \
	-d missing-module-docstring \
	-d too-many-instance-attributes \
	-d too-few-public-methods \
	-d too-many-public-methods \
	-d too-many-arguments \
	-d too-many-locals \
	-d too-many-statements \
	-d too-many-lines \
	-d duplicate-code \
	-d invalid-name \
	-d no-self-use \
	-d import-error \
	-d line-too-long \
	-d fixme \
	-d ungrouped-imports \
	-d raise-missing-from \
	-d consider-using-enumerate \
	-d bad-continuation \
	$(1)
endef

.PHONY: all
all:
	@$(ECHO) "Targets:"
	@$(ECHO) "* wheel       builds a Python .whl"
	@$(ECHO) "* resources   compiles Qt resources"
	@$(ECHO) "* examples    builds examples"
	@$(ECHO) "* test        runs all tests"

.PHONY: wheel
wheel: resources
	@$(PYTHON) -m build

.PHONY: resources
resources: $(RESOURCES_OS)
	@$(RCC) resources/resources.qrc -o ./src/qtmodernredux/resources/qt_resources.py.bak
	@cd src && cd qtmodernredux && cd resources && $(CAT) qt_resources.py.bak >>qt_resources.py
	@cd src && cd qtmodernredux && cd resources && $(RM) qt_resources.py.bak
	@$(ECHO) "finished building resources"

.PHONY: resources_nix
resources_nix:
	@$(ECHO) "# flake8: noqa">./src/qtmodernredux/resources/qt_resources.py
	@$(ECHO) "# type: ignore">>./src/qtmodernredux/resources/qt_resources.py
	@$(ECHO) "# pylint: skip-file">>./src/qtmodernredux/resources/qt_resources.py

.PHONY: resources_win
resources_win:
	@$(ECHO) # flake8: noqa>./src/qtmodernredux/resources/qt_resources.py
	@$(ECHO) # type: ignore>>./src/qtmodernredux/resources/qt_resources.py
	@$(ECHO) # pylint: skip-file>>./src/qtmodernredux/resources/qt_resources.py

.PHONY: examples
examples: resources
	@$(UIC) "src/examples/widgetgallery/mainwindow.ui" -o "src/examples/widgetgallery/mainwindow_ui.py"
	@$(UIC) "src/examples/qdialogs/mainwindow.ui" -o "src/examples/qdialogs/mainwindow_ui.py"
	@$(UIC) "src/examples/titlebar_1/mainwindow.ui" -o "src/examples/titlebar_1/mainwindow_ui.py"
	@$(UIC) "src/examples/titlebar_2/mainwindow.ui" -o "src/examples/titlebar_2/mainwindow_ui.py"
	@$(UIC) "src/examples/splitters/mainwindow.ui" -o "src/examples/splitters/mainwindow_ui.py"
	@$(UIC) "src/examples/customstyle/mainwindow.ui" -o "src/examples/customstyle/mainwindow_ui.py"
	@$(ECHO) "finished building examples"

.PHONY: test
test: resources test_mypy test_pylint test_flake8

.PHONY: test_mypy
test_mypy:
	-@$(call run_mypy, ./src/qtmodernredux)

.PHONY: test_pylint
test_pylint:
	-@$(call run_pylint, ./src/qtmodernredux)

.PHONY: test_flake8
test_flake8:
	-@$(call run_flake8, ./src/qtmodernredux)