# This script generate Farsi wordlist for hunspell
# This requires aspell wordlist tarball and aspell installed on your system
# Aspell is depreacted in Fedora due to https://fedoraproject.org/wiki/Changes/AspellDeprecation

wget ftp://ftp.gnu.org/gnu/aspell/dict/fa/aspell6-fa-0.11-0.tar.bz2
tar -jxvf aspell6-fa-0.11-0.tar.bz2
cd aspell6-fa-0.11-0
export LANG=C.UTF-8
preunzip -d *.cwl
cat *.wl > farsi.wordlist
wordlist2hunspell farsi.wordlist fa_IR
cp -p fa.dat fa_IR.aff
cd ..
mkdir hunspell-fa-0.11
cd hunspell-fa-0.11
cp -p ../aspell6-fa-0.11-0/COPYING ../aspell6-fa-0.11-0/Copyright ../aspell6-fa-0.11-0/README  ../aspell6-fa-0.11-0/doc/ChangeLog .
cp -p ../aspell6-fa-0.11-0/fa_IR.* .
cat > README.fedora << EOF
This source tarball has been created using aspell6-fa-0.11-0 tarball and wordlist2hunspell script.
EOF
cd ..
tar -cf hunspell-fa-0.11.tar hunspell-fa-0.11
bzip2 hunspell-fa-0.11.tar
