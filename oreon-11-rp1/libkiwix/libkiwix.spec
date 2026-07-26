%global source0_hash 6bfee304cf291bc744a70c50d136527c459242909901df7f4cf5137691b886e0

Name: libkiwix
Version: 14.1.1
Release: %autorelease

License: GPL-3.0-or-later
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gtest-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libzim-devel
BuildRequires: mustache-devel
BuildRequires: ninja-build
BuildRequires: pugixml-devel
BuildRequires: zlib-devel

BuildRequires: aria2
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson

Provides: kiwix-lib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kiwix-lib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

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
%{_bindir}/kiwix-compile-*
%{_libdir}/%{name}.so.14*
%{_mandir}/man1/kiwix*.1*

%files devel
%{_includedir}/kiwix
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
