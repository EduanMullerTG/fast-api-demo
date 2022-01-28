source_dir := $(CURDIR)/src

PYTHONPATH += $(source_dir)
ENV_NAME = env
PYTHON_COMMAND ?= python
make_env = $(PYTHON_COMMAND) -m venv $(ENV_NAME)
env_dir = $(CURDIR)/$(ENV_NAME)
bin_dir = $(env_dir)/bin
activate_env = . $(bin_dir)/activate
MIGRATION_REVISION ?= head

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

.PHONY: migrate
migrate:
	PYTHONPATH="$(PYTHONPATH)" 	\
	$(bin_dir)/alembic revision --autogenerate

.PHONY: upgrade
upgrade:
	PYTHONPATH="$(PYTHONPATH)" 	\
	$(bin_dir)/alembic -x data=true upgrade $(MIGRATION_REVISION)

.PHONY: downgrade
downgrade:
	PYTHONPATH="$(PYTHONPATH)" 		\
	$(bin_dir)/alembic -x data=true downgrade $(MIGRATION_REVISION)