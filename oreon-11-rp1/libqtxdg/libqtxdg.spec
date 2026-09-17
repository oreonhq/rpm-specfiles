%global source0_hash 2a19343cffaa869d5001ef8087781beedb25b3f2ebe29f202728a9dc86aaacc8

Name:           libqtxdg
Summary:        QtXdg, a Qt6 implementation of XDG standards
Version:        4.3.0

Release:        4%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://lxqt-project.org
Source0:        https://github.com/lxqt/libqtxdg/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  file-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  qt6-qtbase-private-devel

Requires:       xdg-user-dirs
Requires:       xdg-utils
Obsoletes:      libqtxdg-qt5 <= 1.1.0

%description
%{summary}.

%package devel
Summary:        Qt - development files for qtxdg
Obsoletes:      libqtxdg-qt5-devel <= 1.1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files used for developing and building software that uses qtxdg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libQt6Xdg.so.4
%{_libdir}/libQt6Xdg.so.%{version}
%{_libdir}/libQt6XdgIconLoader.so.4
%{_libdir}/libQt6XdgIconLoader.so.%{version}
%{_sysconfdir}/xdg/lxqt-qtxdg.conf
%{_sysconfdir}/xdg/qtxdg.conf

%files devel
%{_libdir}/libQt6Xdg.so
%{_libdir}/libQt6XdgIconLoader.so
%{_libdir}/pkgconfig/Qt6Xdg.pc
%{_libdir}/pkgconfig/Qt6XdgIconLoader.pc
%{_includedir}/qt6xdg/
%{_includedir}/qt6xdgiconloader/
%{_datadir}/cmake/qt6xdg/
%{_datadir}/cmake/qt6xdgiconloader/
%{_qt6_archdatadir}/plugins/iconengines/libQt6XdgIconPlugin.so

%changelog
%autochangelog
