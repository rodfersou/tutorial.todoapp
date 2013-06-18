#!/bin/bash
rm -rf translated doctrees
for i in `ls locale/pt_BR/LC_MESSAGES/*.po`; do target=translated${i##locale}; mkdir -p ${target%/*}; msgfmt -c -vv --statistics "$i" -o "${target%.po}.mo"; done
make html
