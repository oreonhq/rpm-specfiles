# This script generate Kirghiz wordlist for hunspell
# This requires aspell wordlist tarball and aspell installed on your system
# Aspell is depreacted in Fedora due to https://fedoraproject.org/wiki/Changes/AspellDeprecation

wget http://ftp.gnu.org/gnu/aspell/dict/ky/aspell6-ky-0.01-0.tar.bz2
tar -jxvf aspell6-ky-0.01-0.tar.bz2
cd aspell6-ky-0.01-0
export LANG=C.UTF-8
preunzip -d *.cwl
cat *.wl > kirghiz.wordlist
wordlist2hunspell kirghiz.wordlist ky_KG
cp -p ky_affix.dat ky_KG.aff
cd ..
mkdir hunspell-ky-0.01
cd hunspell-ky-0.01
cp -p ../aspell6-ky-0.01-0/COPYING ../aspell6-ky-0.01-0/Copyright ../aspell6-ky-0.01-0/README ../aspell6-ky-0.01-0/doc/Crawler.txt .
cp -p ../aspell6-ky-0.01-0/ky_KG.* .
cat > README.fedora << EOF
This source tarball has been created using aspell6-ky-0.01-0 tarball and wordlist2hunspell script.
EOF
cd ..
tar -cf hunspell-ky-0.01.tar hunspell-ky-0.01
bzip2 hunspell-ky-0.01.tar
