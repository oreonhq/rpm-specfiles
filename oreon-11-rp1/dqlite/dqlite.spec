%global source0_hash c9468a335aac9755b70f8f92726d84e93b486459767979288aafc43e66b5ff24

Name:           dqlite
Version:        1.17.1
Release:        1%{?dist}
Summary:        Embeddable, replicated and fault tolerant SQL engine

License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/dqlite
Source0:        %{URL}/archive/v%{version}.tar.gz
# https://github.com/ganto/copr-lxc4/issues/24
# https://github.com/canonical/dqlite/issues/643
Patch0:         dqlite-1.17.1-Skip-flaky-tests.patch

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(sqlite3)

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

%autosetup -n %{name}-%{version} -p1

%build
autoreconf -i
%configure --disable-static --enable-build-raft=yes
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdqlite.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libdqlite.so.*

%files devel
%{_libdir}/libdqlite.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h

%changelog
%autochangelog
