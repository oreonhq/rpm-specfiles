%global source0_hash 07307243811d814367500209e73c3a36a7ac1096a04e8b6f608eb0727c0fed54

Name: kiwix-tools
Version: 3.8.1
Release: %autorelease

License: GPL-3.0-or-later
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: docopt-cpp-devel
BuildRequires: libkiwix-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: pugixml-devel
BuildRequires: zlib-devel

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build

%description
The Kiwix tools is a collection of Kiwix related command line
tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS Changelog README.md
%license COPYING
%{_bindir}/kiwix*
%{_mandir}/man1/kiwix*.1*
%{_mandir}/*/man1/kiwix*.1*

%changelog
%autochangelog
