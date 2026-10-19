%global source0_hash f9c1efd5bebbe37fc6e1063db7473ce8df1e3e0be4ff0f43ce04fce57e9c5dd9
%{!?with_x:%global with_x 1}
Summary:        A document formatting system
Name: groff
Version: 1.24.2
Release:        1%{?dist}
License: GPL-3.0-or-later AND GFDL-1.3-or-later AND BSD-4-Clause-UC AND MIT AND X11 AND LicenseRef-Fedora-Public-Domain
URL: http://www.gnu.org/software/groff/
Source0:        https://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz
Patch0: 0001-missing-groff-x11-info-message-when-gxditview-not-fo.patch
Patch1: 0002-load-site-font-and-site-tmac-from-etc-groff.patch
Patch2: 0003-various-security-fixes.patch
Patch4: 0005-do-not-overwrite-docdir.patch
Patch5: 0006-Revert-upstream-change-of-mapping-special-characters.patch
Requires: coreutils, groff-base = %{version}-%{release}
Recommends: psutils
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Requires(preun): /usr/sbin/update-alternatives
Provides: nroff-i18n = %{version}-%{release}
Provides: bundled(gnulib)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\([^.]*\\.pl\\)
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  git
BuildRequires:  libXaw-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  perl-generators
BuildRequires:  psutils
BuildRequires:  texinfo
# /oreon:deps
%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more.

Groff can also be used to format man pages. If you are going to use
groff with the X Window System, you will also need to install the
groff-x11 package.

%package base
Summary: Parts of the groff formatting system required to display manual pages
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Requires(preun): /usr/sbin/update-alternatives
%description base
The groff-base package contains only necessary parts of groff formatting
system which are required to display manual pages, and the groff's default
display device (PostScript).

%package perl
Summary: Parts of the groff formatting system that require Perl
Requires: groff-base = %{version}-%{release}
%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit (font processor
for creating PostScript font files), groffer (tool for displaying groff
files), grog (utility that can be used to automatically determine groff
command-line options), chem (groff preprocessor for producing chemical
structure diagrams), mmroff (reference preprocessor) and roff2dvi
roff2html roff2pdf roff2ps roff2text roff2x (roff code converters).

%if %{with_x}
%package x11
Summary: Parts of the groff formatting system that require X Windows System
Requires: groff-base = %{version}-%{release}
BuildRequires: libXaw-devel, libXmu-devel
BuildRequires: make
Provides: groff-gxditview = %{version}-%{release}
Obsoletes: groff-gxditview < 1.20.1
%description x11
The groff-x11 package contains the parts of the groff text processor
package that require X Windows System. These include gxditview (display
groff intermediate output files on X Window System display) and
xtotroff (converts X font metrics into groff font metrics).
%endif

%package doc
Summary: Documentation for groff document formatting system
BuildArch: noarch
Requires: groff = %{version}-%{release}
%description doc
The groff-doc package includes additional documentation for groff
text processor package. It contains examples, documentation for PIC
language and documentation for creating PDF files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
git init
git config user.email groff-owner@fedoraproject.org
git config user.name "groff owner"
git add .
git commit -n -m "release %{version}"
git am %{patches}

for file in NEWS src/devices/grolbp/grolbp.1.man doc/webpage.ms \
                contrib/mm/*.man contrib/mom/examples/{README.txt,*.mom,mom.vim}; do
    iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
    mv "${file}_" "$file"
done

%build

%configure \
    --docdir=%{_pkgdocdir} \
    --with-appdefdir=%{_datadir}/X11/app-defaults \
    --with-grofferdir=%{_datadir}/%{name}/%{version}/groffer
%make_build
%install
%make_install
mv %{buildroot}%{_bindir}/soelim %{buildroot}%{_bindir}/soelim.%{name}
touch %{buildroot}%{_bindir}/soelim
mv %{buildroot}%{_mandir}/man1/soelim.1 %{buildroot}%{_mandir}/man1/soelim.%{name}.1
touch %{buildroot}%{_mandir}/man1/soelim.1
mv %{buildroot}%{_mandir}/man7/roff.7 %{buildroot}%{_mandir}/man7/roff.%{name}.7
touch %{buildroot}%{_mandir}/man7/roff.7
for file in g{nroff,troff,tbl,pic,eqn,neqn,refer,lookbib,indxbib,soelim} zsoelim; do
    ln -s ${file#?} %{buildroot}%{_bindir}/${file}
    ln -s ${file#?}.1.gz %{buildroot}%{_mandir}/man1/${file}.1.gz
done
rm -f %{buildroot}%{_pkgdocdir}/pdf/mom-pdf.pdf
ln -s ../examples/mom/mom-pdf.pdf %{buildroot}%{_pkgdocdir}/pdf/mom-pdf.pdf
for file in $(find %{buildroot}%{_datadir}/%{name}/%{version}/font/devps -name "*.pfa"); do
    mv ${file} ${file}_
done
sed --in-place 's/\.pfa$/.pfa_/' %{buildroot}%{_datadir}/%{name}/%{version}/font/devps/download
rm -f %{buildroot}%{_infodir}/dir
pushd %{buildroot}%{_pkgdocdir}
    find -name "*.html" | xargs sed -i "/^<!-- CreationDate: /d"
    find -name "*.ps"   | xargs sed -i "/^%%%%CreationDate: /d"
popd
sed --in-place 's|#! /bin/sed -f|#! /usr/bin/sed -f|' %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate/symbol.sed
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

[ -L %{_mandir}/man7/roff.7.gz ] || %{__rm} -f %{_mandir}/man7/roff.7.gz >/dev/null 2>&1 || :
%post

/usr/sbin/update-alternatives --install %{_mandir}/man7/roff.7.gz roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz 300 \
    >/dev/null 2>&1 || :
%preun

if [ $1 -eq 0 ]; then
    /usr/sbin/update-alternatives --remove roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz >/dev/null 2>&1 || :
fi
%postun

if [ $1 -ge 1 ]; then
    if [ "$(readlink /etc/alternatives/roff.7.gz)" == "%{_mandir}/man7/roff.%{name}.7.gz" ]; then
        /usr/sbin/update-alternatives --set roff.7.gz %{_mandir}/man7/roff.%{name}.7.gz >/dev/null 2>&1 || :
    fi
fi
%pre base

[ -L %{_bindir}/soelim ] || %{__rm} -f %{_bindir}/soelim >/dev/null 2>&1 || :
[ -L %{_mandir}/man1/soelim.1.gz ] || %{__rm} -f %{_mandir}/man1/soelim.1.gz >/dev/null 2>&1 || :
%post base

/usr/sbin/update-alternatives --install %{_bindir}/soelim soelim %{_bindir}/soelim.%{name} 300 \
    --slave %{_mandir}/man1/soelim.1.gz soelim.1.gz %{_mandir}/man1/soelim.%{name}.1.gz \
    >/dev/null 2>&1 || :
%preun base

if [ $1 -eq 0 ]; then
    /usr/sbin/update-alternatives --remove soelim %{_bindir}/soelim.%{name} >/dev/null 2>&1 || :
fi
%postun base

if [ $1 -ge 1 ]; then
    if [ "$(readlink /etc/alternatives/soelim)" == "%{_bindir}/soelim.%{name}" ]; then
        /usr/sbin/update-alternatives --set soelim %{_bindir}/soelim.%{name} >/dev/null 2>&1 || :
    fi
fi
%files -f %{oreon_filedir}/main.list
%files -n groff-base -f %{oreon_filedir}/groff-base.list
%files -n groff-perl -f %{oreon_filedir}/groff-perl.list
%files -n groff-x11 -f %{oreon_filedir}/groff-x11.list
%files -n groff-doc -f %{oreon_filedir}/groff-doc.list

%changelog

%autochangelog
