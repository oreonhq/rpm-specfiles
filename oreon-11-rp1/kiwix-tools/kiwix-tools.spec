%global source0_hash 7148522730a66cffb58a3b3674c6cbac548a1f95fd08c5f330565aad70c14d14
Name: kiwix-tools
Version: 3.8.2
Release:        1%{?dist}
License: GPL-3.0-or-later
Summary:        Common code base for all Kiwix ports
URL: https://github.com/kiwix/%{name}
Source0:        https://github.com/kiwix/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  docopt-cpp-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libkiwix-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pugixml-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Kiwix tools is a collection of Kiwix related command line
tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dwerror=false
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
