%global source0_hash 8d13915a36ebbfa8e7b236b350cc81adc714acb217a18e8d8c60747c0ad353f9
Summary:        Converts text and other types of files to PostScript
Name: a2ps
Version: 4.15.8
Release:        3%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.0-or-later
Url: http://www.gnu.org/software/a2ps/
Source0:        http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Source1: ftp://ftp.enst.fr/pub/unix/a2ps/i18n-fonts-0.1.tar.gz
Source2: COPYING
Patch01: a2ps-4.13-conf.patch
Patch02: a2ps-4.13-etc.patch
Patch03: a2ps-4.13-glibcpaper.patch
Patch04: a2ps-sort.patch
Patch05: a2ps-iso5-minus.patch
Patch06: a2ps-perl.patch
Patch07: a2ps-4.13b-numeric.patch
Patch08: a2ps-4.13b-encoding.patch
Patch09: a2ps-4.13b-tilde.patch
Patch10: a2ps-4.13-euckr.patch
Patch11: a2ps-4.13-hebrew.patch
Patch12: a2ps-make-fonts-map.patch
Patch13: a2ps-wdiff.patch
Patch14: a2ps-U.patch
Patch15: a2ps-mb.patch
Patch16: a2ps-4.14-texinfo-nodes.patch
Patch17: a2ps-forward-null.patch
Patch18: a2ps-overrun-dynamic.patch
Patch19: a2ps-overrun-static.patch
Patch20: a2ps-resource-leak.patch
Provides: bundled(gnulib)%(perl -ne 'if($. == 1 and /\A(\d+)-(\d+)-(\d+)/) {print qq{ = $1$2$3}}' %{_defaultdocdir}/gnulib/ChangeLog 2>/dev/null)
Recommends: bzip2
Recommends: groff-perl
Recommends: gzip
Recommends: texinfo
Recommends: texlive-dvips
Recommends: texlive-latex
Recommends: texinfo-tex
Requires: cups-client
Requires: emacs-filesystem
Requires: file
Requires: ghostscript
Requires: psutils
Requires: psutils-perl
Requires: texlive-collection-fontsrecommended
Requires(post): coreutils
Suggests: emacs
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  emacs
BuildRequires:  flex
BuildRequires:  gc-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  ghostscript
BuildRequires:  gnulib-devel
BuildRequires:  gperf
BuildRequires:  groff-perl
BuildRequires:  gzip
BuildRequires:  help2man
BuildRequires:  html2ps
BuildRequires:  libpaper-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  psutils
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  texlive-tex
# /oreon:deps
%description
The a2ps filter converts text and other types of files to PostScript.
A2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1

# use fedora postscript font paths
%patch -P 01 -p1 -b .conf
# add /etc/a2ps in directories searched for config files
%patch -P 02 -p1 -b .etc
%patch -P 03 -p1 -b .glibcpaper
%patch -P 04 -p1 -b .sort
%patch -P 05 -p1 -b .iso5-minus
%patch -P 06 -p1 -b .perl
# Use C locale's decimal point style (bug #53715).
%patch -P 07 -p1 -b .numeric
# Use locale to determine a sensible default encoding (bug #64584).
%patch -P 08 -p1 -b .encoding
# Fix koi8 tilde (bug #66393).
%patch -P 09 -p1 -b .tilde
# Add Korean resource file (bug #81421).
%patch -P 10 -p1 -b .euckr
# Hebrew support (bug #113191).
%patch -P 11 -p1 -b .hebrew
# Fix problems in make_fonts_map script (bug #142299).  Patch from
# Michal Jaegermann.
%patch -P 12 -p1 -b .make-fonts-map
# Make pdiff default to not requiring wdiff (bug #68537).
%patch -P 13 -p1 -b .wdiff
# Make pdiff use diff(1) properly (bug #156916).
%patch -P 14 -p1 -b .U
# Fixed multibyte handling (bug #212154).
%patch -P 15 -p1 -b .mb
# Remove dots in node names, patch from Vitezslav Crhonek (Bug #445971)
%patch -P 16 -p1 -b .nodes
# Coverity fix (forward-null).
%patch -P 17 -p1 -b .forward-null
# Coverity fix (overrun-dynamic).
%patch -P 18 -p1 -b .overrun-dynamic
# Coverity fix (overrun-static).
%patch -P 19 -p1 -b .overrun-static
# Coverity fix (resource-leak).
%patch -P 20 -p1 -b .resource-leak

for file in AUTHORS ChangeLog; do
  iconv -f latin1 -t UTF-8 < $file > $file.utf8
  touch -c -r $file $file.utf8
  mv $file.utf8 $file
done

autoreconf -fi

mv doc/encoding.texi doc/encoding.texi.utf8
iconv -f KOI-8 -t UTF-8 doc/encoding.texi.utf8 -o doc/encoding.texi

# Fix reference to a2ps binary (bug #112930).
sed -i -e "s,/usr/local/bin,%{_bindir}," contrib/emacs/a2ps.el

chmod 644 encoding/iso8.edf.hebrew
chmod 644 encoding/euc-kr.edf.euckr

%build

sed -e "s!@date@!`date -r NEWS`!" etc/README.in > etc/README.in.tmp
touch -c -r etc/README.in etc/README.in.tmp
mv etc/README.in.tmp etc/README.in
EMACS=emacs %configure \
  --with-medium=_glibc \
  --enable-kanji \
  --with-lispdir=%{_emacs_sitelispdir}/%{name}
find . -name "*.info*" -exec rm -f {} \;
find src lib -name '*.l' -exec touch {} \;
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install INSTALL='install -p'
touch -r etc/README.in %{buildroot}%{_datadir}/a2ps/README
mkdir -p %{buildroot}%{_sysconfdir}/a2ps
mkdir -p %{buildroot}%{_datadir}/a2ps/{afm,fonts}
pushd i18n-fonts-0.1/afm
install -p -m 0644 *.afm %{buildroot}%{_datadir}/a2ps/afm
pushd ../fonts
install -p -m 0644 *.pfb %{buildroot}%{_datadir}/a2ps/fonts
popd
popd
rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_defaultlicensedir}/%{name}/COPYING
for lang in af be bg ca cs da de el eo es et eu fi fr ga gl hu it ja ka ko ms nb nl pl pt pt_BR ro ru rw sk sl sr sv tr uk vi zh_CN zh_TW
do
  mv %{buildroot}/usr/share/locale/$lang/LC_MESSAGES/a2ps{-gnulib,}.mo
done
%find_lang %name
%oreon_autofiles main

%post

%{?ldconfig}
(cd %{_datadir}/a2ps/afm;
 ./make_fonts_map.sh > /dev/null 2>&1 || /bin/true
 if [ -f fonts.map.new ]; then
   mv fonts.map.new fonts.map
 fi
)
exit 0
%ldconfig_postun
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
