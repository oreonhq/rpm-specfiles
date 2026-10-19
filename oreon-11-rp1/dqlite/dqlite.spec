%global source0_hash 7a9087460f3296313379e95a25761c88081c508ae0742bec6fb63e895eb807a9
Name:           dqlite
Version:        1.18.7
Release:        1%{?dist}
Summary:        Embeddable, replicated and fault tolerant SQL engine
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/dqlite
Source0:        https://github.com/canonical/%{name}/archive/v%{version}.tar.gz
Patch0:         dqlite-1.17.1-Skip-flaky-tests.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
dqlite is a C library that implements an embeddable and replicated SQL database
engine with high-availability and automatic failover.

%package devel
Summary:        Development libraries for dqlite
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and library for dqlite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -i
%configure --disable-static --enable-build-raft=yes
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libdqlite.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n dqlite-devel -f %{oreon_filedir}/dqlite-devel.list

%changelog

%autochangelog
