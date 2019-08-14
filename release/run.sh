#!/bin/sh

function run
{
	mkdir cache
	cd cache
	unzip ../wet-$1.zip
	cd stor
	./run.sh
	cd ../..
	rm -rv cache
}
