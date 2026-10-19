%global source0_hash ceec5d8c284cad8f7abeda2862ee6b815431a38d664eed24f3a98a10294f4e42
Name:		hidviz
Version:	0.2.1
Release:        1%{?dist}
Summary:        A tool for in-depth analysis of USB HID devices communication
License:	GPL-3.0-or-later
URL:		https://hidviz.org/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme
Patch:		hidviz-0.2.1-cmake-4-fix.patch
# oreon:deps
BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Hidviz is a GUI application for in-depth analysis of USB HID class devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
