export BASH_COLOR_PROMPT_DIR = ../..

check:
	make -C $(BASH_COLOR_PROMPT_DIR)
	rm -f logs/*
	bats --timing --gather-test-outputs-in logs test.bats
