%global source0_hash 338ba2e83360f41ded96a0ceb132db9beaaf15018b36101be2bae8bb239017d9
Name:           latex2rtf
Version:        2.3.18a
Release:        1%{?dist}
Summary:        LaTeX to RTF converter that handles equations, figures, and cross-references
License:        GPL-2.0-or-later
URL:            http://latex2rtf.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}a.tar.gz
Patch1:         latex2rtf-a4wide.patch
Requires:       gawk
Requires:       grep
Requires:       ImageMagick
Requires:       sed
Requires:       /usr/bin/eps2eps
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-courier
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-psfrag
BuildRequires:  texlive-times
# /oreon:deps
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

%make_build %{name} CFLAGS="%{optflags} -DUNIX -fsigned-char" LDFLAGS="%{?__global_ldflags}" PREFIX=%{_prefix}
%install
%make_install -j1 install-info PREFIX=%{_prefix}
rm -frv %{buildroot}%{_infodir}/dir
%oreon_autofiles main

%check

RTFPATH=`pwd`/cfg \
%{__make} check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
