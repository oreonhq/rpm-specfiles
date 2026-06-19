%global source0_hash none

%undefine __cmake_in_source_build

%global stable_plasma stable
%global plasma_ver 6.7.0

Name:           libkscreen
Version:        %{plasma_ver}
Release:        4%{?dist}
Summary:        KDE screen management library

License:        LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC0-1.0
URL:            https://invent.kde.org/plasma/libkscreen

Source0:        https://download.kde.org/%{stable_plasma}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules >= 6.22.0
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-dpms)

Requires:       kf6-filesystem

%description
libkscreen provides runtime support for listing outputs, reading display
configuration, Wayland and X11 backends, and helpers used by Plasma
(powerdevil, kscreen, kwin, etc.).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)

%description    devel
Headers and CMake package KF6Screen for software that links libkscreen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libkscreen-%{version} -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=OFF
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose

%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose

%find_lang_kf6 libkscreen6_qt

%ldconfig_scriptlets

%files -f libkscreen6_qt.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_datadir}/qlogging-categories6/libkscreen.categories
%{_kf6_libdir}/libKF6Screen.so.8*
%{_kf6_libdir}/libKF6Screen.so.%{version}
%{_kf6_libdir}/libKF6ScreenDpms.so.8*
%{_kf6_libdir}/libKF6ScreenDpms.so.%{version}
%{_kf6_plugindir}/kscreen/*.so
%{_kf6_libexecdir}/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service
%{_userunitdir}/plasma-kscreen.service
%{_bindir}/kscreen-doctor
%{_datadir}/zsh/site-functions/_kscreen-doctor

%files devel
%{_kf6_includedir}/KScreen/
%{_kf6_libdir}/libKF6Screen.so
%{_kf6_libdir}/libKF6ScreenDpms.so
%{_kf6_libdir}/cmake/KF6Screen/
%{_libdir}/pkgconfig/KF6Screen.pc
%{_kf6_includedir}/kscreen_version.h


%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-4
- Package versioned .so, zsh completion; turn off QCH (no qt6 help install)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-3
- Fix kscreen backend glob (no double kf6 under %%{_kf6_plugindir})

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Plasma 6.6.3 source, backends, launcher, translations (KF6Screen)
