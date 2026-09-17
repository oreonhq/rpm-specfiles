%global source0_hash 0937b21cd7d0c600e907871784181a2d152a6f8a619ff092d760c26f796e4315

Name: libzim
Version: 9.4.1
Release: %autorelease

License: GPL-2.0-only AND Apache-2.0 AND BSD-3-Clause
Summary: Reference implementation of the ZIM specification

URL: https://github.com/openzim/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gtest-devel
BuildRequires: libicu-devel
BuildRequires: libzstd-devel
BuildRequires: xapian-core-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build

Provides: zimlib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: zimlib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/%{name}.so.9*

%files devel
%{_includedir}/zim
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
