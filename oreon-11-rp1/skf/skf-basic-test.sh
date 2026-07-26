#!/bin/sh

set -x

a_utf8=$(echo -e '\xe3\x81\x82')
a_eucjp=$(echo -e '\xa4\xa2')
# FIXME
a_eucjp_escaped='\xa4\xa2'

# Binary
echo "Checking Binary"
a_from_shift_jis=$(echo $a_eucjp | skf -s | iconv -f shift-jis -t utf-8)
a_from_iso=$(echo $a_eucjp | skf --oc=iso-2022-jp | iconv -f iso-2022-jp -t utf-8)
a_from_utf8=$(echo $a_eucjp | skf -z)

if [ "$a_from_shift_jis" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_iso" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_utf8" != "$a_utf8" ] ; then exit 1 ; fi

echo "Checking python2"
if [ "x$CHECK_PYTHON2" != "xno" ] ; then
  export PYTHONPATH=$python2PATH
  a_from_shift_jis=$(python2 -c "import skf ; print (skf.convert('-s', \"$a_eucjp\"))" | iconv -f shift-jis -t utf-8)
  a_from_iso=$(python2 -c "import skf ; print (skf.convert('--oc=iso-2022-jp', \"$a_eucjp\"))" | iconv -f iso-2022-jp -t utf-8)
  a_from_utf8=$(python2 -c "import skf ; print (skf.convert('-z', \"$a_eucjp\"))")

  if [ "$a_from_shift_jis" != "$a_utf8" ] ; then exit 1 ; fi
  if [ "$a_from_iso" != "$a_utf8" ] ; then exit 1 ; fi
  if [ "$a_from_utf8" != "$a_utf8" ] ; then exit 1 ; fi
fi

# python3
# skip this for now
if ( which python3 ) ; then
   # Not check for now
   echo "Checking python3"
   export PYTHONPATH=$python3PATH
   #FIXME
   #FIXME
   #The following 3 lines need fixing
   #a_from_shift_jis=$(python3 -c "import skf ; print (skf.convert('-s', b\"$a_eucjp_escaped\"))" | iconv -f shift-jis -t utf-8)
   a_from_shift_jis=$(python3 -c "import skf ; print (skf.convert('-s', b\"$a_eucjp_escaped\"))")
   a_from_shift_jis=$(echo "${a_from_shift_jis}" | sed -n -e "s@^.*bytearray(b'\(.*\)')@\1@p")
   a_from_shift_jis=$(echo -e $a_from_shift_jis | iconv -f shift-jis -t utf-8)

   a_from_iso=$(python3 -c "import skf ; print (skf.convert('--oc=iso-2022-jp', b\"$a_eucjp_escaped\"))")
   a_from_iso=$(echo "${a_from_iso}" | sed -n -e "s@^.*bytearray(b'\(.*\)')@\1@p")
   a_from_iso=$(echo -e $a_from_iso | iconv -f iso-2022-jp -t utf-8)

   a_from_utf8=$(python3 -c "import skf ; print (skf.convert('-z', b\"$a_eucjp_escaped\"))")
   a_from_utf8=$(echo "${a_from_utf8}" | sed -n -e "s@^.*bytearray(b'\(.*\)')@\1@p")
   a_from_utf8=$(echo -e $a_from_utf8)

   if [ "$a_from_shift_jis" != "$a_utf8" ] ; then exit 1 ; fi
   if [ "$a_from_iso" != "$a_utf8" ] ; then exit 1 ; fi
   if [ "$a_from_utf8" != "$a_utf8" ] ; then exit 1 ; fi
fi

# perl
echo "Checking perl"
a_from_shift_jis=$(perl -e "use skf ; print skf::convert('-s', \"$a_eucjp\")" | iconv -f shift-jis -t utf-8)
a_from_iso=$(perl -e "use skf ; print skf::convert('--oc=iso-2022-jp', \"$a_eucjp\")" | iconv -f iso-2022-jp -t utf-8)
a_from_utf8=$(perl -e "use skf ; print skf::convert('-z', \"$a_eucjp\")")

if [ "$a_from_shift_jis" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_iso" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_utf8" != "$a_utf8" ] ; then exit 1 ; fi


# ruby
echo "Checking ruby"
ruby -e 'puts $:'

a_eucjp_arr='[0xa4, 0xa2]'

a_from_shift_jis=$(ruby -e "require 'skf' ; puts Skf.convert('-s', $a_eucjp_arr.pack(\"C*\"))" | iconv -f shift-jis -t utf-8)
a_from_iso=$(ruby -e "require 'skf' ; puts Skf.convert('--oc=iso-2022-jp', $a_eucjp_arr.pack(\"C*\"))" | iconv -f iso-2022-jp -t utf-8)
a_from_utf8=$(ruby -e "require 'skf' ; puts Skf.convert('-z', $a_eucjp_arr.pack(\"C*\"))")

if [ "$a_from_shift_jis" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_iso" != "$a_utf8" ] ; then exit 1 ; fi
if [ "$a_from_utf8" != "$a_utf8" ] ; then exit 1 ; fi
