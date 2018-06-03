#!/bin/bash

for f in walk_across walk_across walk_across
do
   file=`echo $f.py`
   echo Running file $file
   pred $file
   if [ $? -ne 1 ]; then
      exit $?
   fi
done
