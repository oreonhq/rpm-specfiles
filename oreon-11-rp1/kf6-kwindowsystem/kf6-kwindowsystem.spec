%global		framework kwindowsystem

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	4%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:	CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# Upstream patches

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xrender)
BuildRequires:  wayland-devel
BuildRequires:  egl-wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:	fdupes
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
Requires:	kf6-filesystem

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package	html
Summary:	Developer Documentation files for %{name} in HTML format
BuildArch:	noarch
%description	html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

# Qt6 qdoc: list all files under %{_qt6_docdir} except tags/index (-devel owns those).
: > %{_builddir}/%{framework}-qt6doc.files
if [ -d "%{buildroot}%{_qt6_docdir}" ]; then
  find "%{buildroot}%{_qt6_docdir}" -type f \
    ! -name '*.tags' ! -name '*.index' \
    | sed "s#^%{buildroot}##" >> %{_builddir}/%{framework}-qt6doc.files
fi
LC_ALL=C sort -u -o %{_builddir}/%{framework}-qt6doc.files %{_builddir}/%{framework}-qt6doc.files

%find_lang_kf6 kwindowsystem6_qt
%fdupes %{buildroot}%{_kf6_includedir}

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6WindowSystem.so.*
%dir %{_kf6_plugindir}/kwindowsystem/
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_qmldir}/org/kde/kwindowsystem
%{_qt6_plugindir}/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/cmake/KF6WindowSystem/
%{_kf6_libdir}/pkgconfig/KF6WindowSystem.pc

%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files html -f %{_builddir}/%{framework}-qt6doc.files

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

