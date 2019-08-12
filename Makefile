
install:
	@python3 install.py
run:
	@cd stor && python3 vmwet.pyc
	@cd ..
clean:
	@rm -rv jobs/* stor/vmwet.pyc init.py
	@mkdir -pv jobs/job_commands
	@> init.py

install-commands:
	@python3 install_commands.py

clean-commands:
	@rm -v jobs/job_commands/* commands.py

all:
	@make install-commands && make clean-commands && make install-commands && make clean && make && make run