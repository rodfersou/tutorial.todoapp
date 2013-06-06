Update translations
===================

$ cd docs
$ make gettext
$ for i in `ls locale/pt_BR/LC_MESSAGES/*.po`; do target=translated${i##locale}; mkdir -p ${target%/*}; msgfmt -c -vv --statistics "$i" -o "${target%.po}.mo"; done

Build localized documentation
=============================

#. change ``locale_dirs`` in conf.py from ["locale/"] to ["translated/"]
#. change ``language`` in conf.py to your language
#. run bin/sphinxbuilder
#. your docs are now in docs/html
