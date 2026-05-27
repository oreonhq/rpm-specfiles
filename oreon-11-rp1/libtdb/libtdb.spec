%global source0_hash fba09d8df1f1b9072aeae8e78b2bd43c5afef20b2f6deefa633aa14a377a8dd2

Name:            libtdb
Version:         1.4.15
Release:         %autorelease
Summary:         The tdb library
License:         LGPL-3.0-or-later
URL:             http://tdb.samba.org/
Source0:         http://samba.org/ftp/tdb/tdb-%{version}.tar.gz
Source1:         http://samba.org/ftp/tdb/tdb-%{version}.tar.asc
# gpg2 --no-default-keyring --keyring ./tdb.keyring --recv-keys 9147A339719518EE9011BCB54793916113084025
Source2:         tdb.keyring

BuildRequires: make
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: python3-devel

Provides: bundled(libreplace)
Obsoletes: python2-tdb < 1.4.2-1

%description
A library that implements a trivial database.

%package         devel
Summary:         Header files need to link the Tdb library

Requires: libtdb = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Tdb library.

%package -n tdb-tools
Summary:         Developer tools for the Tdb library

Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python3-tdb
Summary: Python3 bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python3-tdb}

%description -n python3-tdb
Python3 bindings for libtdb

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n tdb-%{version} -p1

%build
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
# workaround https://gitlab.com/ita1024/waf/-/issues/2472
export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

%check
%make_build check

%install
%make_install

%files
%license LICENSE
%{_libdir}/libtdb.so.*

%files devel
%doc docs/README
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%files -n python3-tdb
%{python3_sitearch}/__pycache__/_tdb_text.cpython*.py[co]
%{python3_sitearch}/tdb.cpython*.so
%{python3_sitearch}/_tdb_text.py

%ldconfig_scriptlets

%changelog
* Wed Apr 22 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.15-1
- Prepare for Oreon 11 (RP1)
