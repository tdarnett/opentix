# Location of SmartPy CLI
ifeq ($(SMARTPY_DIR),)
  SMARTPY_DIR:=~/smartpy-cli
endif

SMARTPY:=${SMARTPY_DIR}/SmartPy.sh

SHELL:=bash

DEFAULT_TARGET:=nft

# TARGET, if none is given in the environment
ifeq ($(TARGET),)
  TARGET:=${DEFAULT_TARGET}
endif

export PYTHONPATH:=.:$(PYTHONPATH)

# Contracts source
SC_SRC_DIR:=$(realpath ./contracts)
# Contracts test source
SC_TEST_DIR:=$(realpath ./tests)
# Output directory, absolute path
SC_OUT_DIR:=$(realpath ./output)
# Compile and test working directory
COMPILE_DIR:=$(realpath .)

define COMPILE
	cd ${COMPILE_DIR}; ${SMARTPY} compile ${SC_SRC_DIR}/$(strip $1).py ${SC_OUT_DIR}/contracts/$(strip $1) --purge --html
endef

define TEST
	cd ${COMPILE_DIR}; ${SMARTPY} test ${SC_TEST_DIR}/$(strip $1)_test.py ${SC_OUT_DIR}/tests/$(strip $1) --purge --html
endef

## Compile the TARGET contract
# Usage example (bash): "TARGET=xyzContract make compile;"
compile:
	$(call COMPILE, ${TARGET})

## Execute tests on TARGET contract
test:
	$(call TEST, ${TARGET})

compile_all:
	$(call COMPILE, nft)

test_all:
	$(call TEST, nft)
