%global source0_hash ceec5d8c284cad8f7abeda2862ee6b815431a38d664eed24f3a98a10294f4e42

Name:		hidviz
Version:	0.2.1
Release:	3%{?dist}
Summary:	A tool for in-depth analysis of USB HID devices communication
License:	GPL-3.0-or-later
URL:		https://hidviz.org/
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt6-qtbase-devel
BuildRequires:	protobuf-devel
BuildRequires:	libusbx-devel
BuildRequires:	asio-devel
# Already fixed in upstream
Patch:		hidviz-0.2.1-cmake-4-fix.patch

%description
Hidviz is a GUI application for in-depth analysis of USB HID class devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/libhid*.so*
%{_libexecdir}/libhidx_server_daemon
%{_datadir}/icons/hicolor/128x128/apps/hidviz.png
%{_datadir}/applications/hidviz.desktop

%changelog
%autochangelog
