#!/bin/sh -eux

# array of keymaps that differ
DIFFERS=""

# convert X keyboard layouts to console keymaps
mkdir -p keymaps/xkb
perl xml2lst.pl < /usr/share/X11/xkb/rules/base.xml > layouts-variants.lst
while read line; do
  XKBLAYOUT=`echo "$line" | cut -d " " -f 1`
  echo "$XKBLAYOUT" >> layouts-list.lst
  XKBVARIANT=`echo "$line" | cut -d " " -f 2`
  ckbcomp -rules base "$XKBLAYOUT" "$XKBVARIANT" | gzip > keymaps/xkb/"$XKBLAYOUT"-"$XKBVARIANT".map.gz
done < layouts-variants.lst

# convert X keyboard layouts (plain, no variant)
cat layouts-list.lst | sort -u >> layouts-list-uniq.lst
while read line; do
  ckbcomp -rules base "$line" | gzip > keymaps/xkb/"$line".map.gz
done < layouts-list-uniq.lst

# wipe converted layouts which cannot input ASCII (#1031848)
zgrep -L "U+0041" keymaps/xkb/* | xargs rm -f

# wipe the xkb-converted georgian layout, it is unusable, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=2336875
# https://src.fedoraproject.org/rpms/kbd/pull-request/2#comment-239318
# do it only if it's already wiped in kbd
if [ ! -f "/lib/kbd/keymaps/xkb/ge.map.gz" ]; then
  rm -f keymaps/xkb/ge.map.gz
fi

# fix converted cz layout - add compose rules, if exists
if [ -f "keymaps/xkb/cz.map.gz" ]; then
  gunzip keymaps/xkb/cz.map.gz
  patch keymaps/xkb/cz.map < cz-map.patch
  gzip keymaps/xkb/cz.map
fi

# compare just created keymaps with kbd counterparts
for keymap in /lib/kbd/keymaps/xkb/*; do
  keymap_name=$(basename ${keymap})
  if ! diff <(zcat "$keymap") <(zcat keymaps/xkb/"$keymap_name") ; then
    DIFFERS="${DIFFERS} ${keymap_name}"
  fi
done

# fail if any keymap differs and print list of them
if [ -n "$DIFFERS" ]; then
  echo "Difference found in:"
  for differ in ${DIFFERS}; do
    echo "- ${differ}"
  done
  exit 1
fi
