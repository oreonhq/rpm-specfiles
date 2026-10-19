%global source1_hash 18c2fd8e8ae2346fc24dc0957c499892cedc8004bc7a3061e90b244f1b2720a6
%global source0_hash fba09d8df1f1b9072aeae8e78b2bd43c5afef20b2f6deefa633aa14a377a8dd2
Name:            libtdb
Version:         1.4.15
Release:        1%{?dist}
Summary:        The tdb library
License:         LGPL-3.0-or-later
URL:             http://tdb.samba.org/
Source0:        http://samba.org/ftp/tdb/tdb-%{version}.tar.gz
Source1:        http://samba.org/ftp/tdb/tdb-%{version}.tar.asc
Source2:         tdb.keyring
Provides: bundled(libreplace)
Obsoletes: python2-tdb < 1.4.2-1
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir tdb-%{version}
%oreon_prep
%build

zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace
%make_build
%check

%make_build check
%install
%make_install
%oreon_autofiles tdb-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-tdb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libtdb-devel -f %{oreon_filedir}/libtdb-devel.list
%files -n tdb-tools -f %{oreon_filedir}/tdb-tools.list
%files -n python3-tdb -f %{oreon_filedir}/python3-tdb.list

%changelog

* Wed Apr 22 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.15-1
- Prepare for Oreon 11 (RP1)
