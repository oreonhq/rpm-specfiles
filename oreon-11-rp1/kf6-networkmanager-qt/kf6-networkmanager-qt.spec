%global source0_hash f6ba5f54d413ea0b2642207a6ebd0803e7cb8392b91fcf8a1679fd0c21062865

%undefine __cmake_in_source_build

%global framework networkmanager-qt

%global stable_kf6 stable
%global majmin_ver_kf6 6.30

%ifarch aarch64
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif

Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        A Tier 1 KDE Frameworks 6 module that wraps NetworkManager DBus API
License:        LGPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND CC0-1.0
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  extra-cmake-modules >= 6.30.0

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

# Other
BuildRequires:  pkgconfig(libnm)
Recommends:     NetworkManager

%description
A Tier 1 KDE Frameworks 6 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       pkgconfig(libnm)
%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6NetworkManagerQt.so.6
%{_kf6_libdir}/libKF6NetworkManagerQt.so.%{version}
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/kde-qmlmodule.version
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/networkmanagerqtqml.qmltypes
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/qmldir

%files devel
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so
%{_kf6_libdir}/cmake/KF6NetworkManagerQt/


%changelog
%autochangelog
