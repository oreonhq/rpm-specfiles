%global source0_hash c6d30b395a8773ede782afc83717aeb577aedcddc91090241d242daee27ef667

%define _lto_cflags %{nil}
%undefine _package_note_file

Name:           gnucobol
Version:        3.2
Release:        9%{?dist}
Summary:        COBOL compiler

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-only AND FSFAP AND GPL-2.0-or-later AND LGPL-3.0-or-later

URL:            https://www.gnu.org/software/gnucobol/
Source0:        https://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source3:        https://www.itl.nist.gov/div897/ctg/suites/newcob.val.Z
Source4:        http://downloads.sourceforge.net/%{name}/contrib/esql/%{name}-sql-3.0.tar.gz

# https://sourceforge.net/p/gnucobol/bugs/941/
Patch0:         xml-parser.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  readline-devel
BuildRequires:  libdb-devel
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  perl-interpreter
BuildRequires:  libxml2-devel
BuildRequires:  json-c-devel
BuildRequires: make
# esql
BuildRequires: unixODBC-devel
BuildRequires: gcc-c++

Requires:       gcc
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       redhat-rpm-config
Requires:       libcob = %{version}

%description
COBOL compiler, which translates COBOL
programs to C code and compiles them using GCC.

%package -n libcob
Summary:        GnuCOBOL runtime library
License:        LGPL-3.0-or-later

%description -n libcob
%{summary}.
Runtime libraries for GnuCOBOL

%package esql
Summary:        ESQL for GnuCOBOL
License:        LGPL-3.0-or-later

%description esql
%{summary}.
ESQL for GnuCOBOL

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0
cp %{SOURCE3} tests/cobol85/

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --enable-hardening --with-db --with-xml2 --with-curses=ncursesw --with-json=json-c

%make_build

iconv -c --to-code=UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

tar -xzf %{SOURCE4}
pushd gnucobol-sql-3.0/
%configure --enable-static=no
%make_build
popd

%install
%make_install
find %{buildroot}/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_infodir}/dir

pushd gnucobol-sql-3.0/
%make_install
popd

%find_lang %{name}

%check
(make check CFLAGS="%optflags -O" || make check TESTSUITEFLAGS="--recheck --verbose" || echo "Warning, unexpected results")
make test CFLAGS="%optflags -O"

%files -f %%{name}.lang
%license COPYING.DOC COPYING
%doc AUTHORS ChangeLog
%doc NEWS README THANKS
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_includedir}/*
%{_libdir}/%{name}
%{_libdir}/libcob.so
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info.*
%{_mandir}/man1/cobc.1.*
%{_mandir}/man1/cobcrun.1.*
%{_mandir}/man1/cob-config.1.*

%files -n libcob
%license COPYING.LESSER
%{_libdir}/libcob.so.4*
%{_libdir}/gnucobol/CBL_OC_DUMP.so

%files esql
%{_bindir}/esqlOC
%{_libdir}/libocsql.so*

%changelog
%autochangelog
