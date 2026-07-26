%global source0_hash 338ba2e83360f41ded96a0ceb132db9beaaf15018b36101be2bae8bb239017d9

Name:           latex2rtf
Version:        2.3.18
Release:        17%{?dist}
Summary:        LaTeX to RTF converter that handles equations, figures, and cross-references
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://latex2rtf.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}a.tar.gz
# Do not use (non-existent on EL7) a4wide paper style in tests
Patch1:         latex2rtf-a4wide.patch
BuildRequires:  make
BuildRequires:  gcc
# For running the tests
BuildRequires:  ImageMagick
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)
BuildRequires:  texlive-courier
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-psfrag
BuildRequires:  texlive-times
Requires:       gawk
Requires:       grep
# For converting images, /usr/bin/convert
Requires:       ImageMagick
Requires:       sed
# For latex2png, ghostscript
Requires:       /usr/bin/eps2eps
# Including netpbm, latex2html, some sty files might be missing from userland
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
%if 0%{?fedora}
Requires:       texlive-collection-latexextra
%endif

%description
LaTeX2rtf is a translator program which is intended to translate a LaTeX
document (precisely: the text and a limited subset of LaTeX tags) into the RTF
format which can be imported by several text processors (including Microsoft
Word for Windows and Word for Macintosh). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .a4wide

# fix Makefile
sed -i -e '/^\.PHONY/d' Makefile

# Get rid of iffy permissions.
chmod a-x cfg/*.cfg

# Delete prebuilt objects in case of subtle failure.
find -name "*.o" -delete -print

# Fix permissions again for normal files.
find . -type f -exec chmod 644 {} \;
chmod 755 test/bracecheck
chmod 755 scripts/latex2png

# Change encoding of documentation.
for txtfile in ChangeLog Copyright; do
 iconv -f ASCII -t UTF-8 $txtfile >$txtfile.new && \
 touch -r $txtfile $txtfile.new && \
 mv $txtfile{.new,} 
done

%build
# Set the necessary config options, including location of config files
# -fsigned-char is useful for special arches, don't forget it.
%make_build %{name} CFLAGS="%{optflags} -DUNIX -fsigned-char" LDFLAGS="%{?__global_ldflags}" PREFIX=%{_prefix}

%install
%make_install -j1 install-info PREFIX=%{_prefix}
# Remove unnecessary file from infodir
rm -frv %{buildroot}%{_infodir}/dir

%check
RTFPATH=`pwd`/cfg \
%{__make} check

%files
%doc ChangeLog doc/latex2rtf.pdf doc/latex2rtf.html doc/credits
%license Copyright doc/copying.txt
%{_bindir}/latex2png
%{_bindir}/latex2rtf
%{_datadir}/latex2rtf/
%{_infodir}/latex2rtf.info.*
%{_mandir}/man1/latex2png.1.*
%{_mandir}/man1/latex2rtf.1.*

%changelog
%autochangelog
