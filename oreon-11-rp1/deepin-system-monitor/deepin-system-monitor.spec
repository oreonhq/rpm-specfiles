%global source0_hash bda9a74ab92b8261f6c9c7e9faada0e019da17126b9c7d9710c5daeafcbc0cc6
Name:           deepin-system-monitor
Version:        6.5.47
Release:        1%{?dist}
Summary:        A more user-friendly system monitor
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Recommends:     deepin-manual
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i 's|lib/|${CMAKE_INSTALL_LIBDIR}/|' deepin-system-monitor-plugin/CMakeLists.txt

%build

export CXXFLAGS="%{optflags} -Wno-error=incompatible-pointer-types"
%cmake -GNinja -DUSE_DEEPIN_WAYLAND=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
