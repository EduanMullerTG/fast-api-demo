source_dir := $(CURDIR)/src

PYTHONPATH += $(source_dir)
ENV_NAME = env
PYTHON_COMMAND ?= python
make_env = $(PYTHON_COMMAND) -m venv $(ENV_NAME)
env_dir = $(CURDIR)/$(ENV_NAME)
bin_dir = $(env_dir)/bin
activate_env = . $(bin_dir)/activate
dotenv_file = .env

define create-env
	@echo Creating $@...
	$(make_env)
	$(bin_dir)/pip install pip
	$(bin_dir)/pip install pip-tools
endef

env:
	$(create-env)

.PHONY: install
install: env
	$(bin_dir)/pip-sync requirements.txt