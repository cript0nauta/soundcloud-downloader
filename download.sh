#!/bin/sh
for cancion in $(cat canciones.txt)
do
	python soundcloud.py "$cancion"
done
