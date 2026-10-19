%global source0_hash ab98c40b867d01272bdf9babc777c8db72fe504d1c87bea4eceb15e33cd12042
%global repo dde-calendar
%global __provides_exclude_from ^%{_libdir}/deepin-aiassistant/.*\\.so$
Name:           deepin-calendar
Version:        6.6.3
Release:        1%{?dist}
Summary:        Calendar for Deepin Desktop Environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Recommends:     deepin-manual
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libical)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Calendar for Deepin Desktop Environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

sed -i 's|lib/deepin-aiassistant/|${CMAKE_INSTALL_LIBDIR}/deepin-aiassistant/|' schedule-plugin/CMakeLists.txt

%build

%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
install -pDm644 calendar-client/assets/dde-calendar/calendar/common/dde-calendar.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/dde-calendar.svg
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
