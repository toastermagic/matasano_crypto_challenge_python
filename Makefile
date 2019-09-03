default: test

SUBDIRS=$(shell ls -d */)

test:
	@for dir in $(SUBDIRS); do make -C $$dir; done
