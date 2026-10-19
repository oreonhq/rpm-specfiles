%global source0_hash 385f91a0b542ebe8b81c8f8500310dcd575fd028ea0cd2ede8807fa920dcf604
Name:           raft
Version:        0.22.1
Release:        5%{?dist}
Summary:        C implementation of the Raft consensus protocol
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://raft.readthedocs.io/
Source0:        https://%{name}.readthedocs.io//archive/v%{version}.tar.gz
Conflicts:      dqlite < 1.16.0-2
Conflicts:      cowsql < 1.15.4
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  python-sphinx
# /oreon:deps
%description
Fully asynchronous C implementation of the Raft consensus protocol. It consists
of a core part that implements the core Raft algorithm logic and a pluggable
interface defining the I/O implementation for networking and disk persistence.

%package benchmark
Summary:        Benchmark operating system disk write performance
BuildRequires:  pkgconfig(liburing)
%description benchmark
Benchmark operating system disk write performance.

%package devel
Summary:        Development libraries for raft
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and library for raft.

%package doc
Summary:        C-Raft documentation
BuildArch:      noarch
BuildRequires:  python-sphinx
%description doc
This package contains the C-Raft documentation in HTML format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

autoreconf -i
%configure --disable-static --enable-benchmark
%make_build
sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html
%install
%make_install
rm -f %{buildroot}%{_libdir}/libraft.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%global _smp_mflags -j1
%make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n raft-benchmark -f %{oreon_filedir}/raft-benchmark.list
%files -n raft-devel -f %{oreon_filedir}/raft-devel.list
%files -n raft-doc -f %{oreon_filedir}/raft-doc.list

%changelog

%autochangelog
