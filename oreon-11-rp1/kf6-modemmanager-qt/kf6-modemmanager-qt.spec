%global framework modemmanager-qt

Name:    kf6-%{framework}
Version: 6.24.0
Release: 2%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License: GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ModemManager-devel >= 1.0.0
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

%description
A Qt 6 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt6-qtbase-devel
%description    devel
Qt 6 libraries and header files for developing applications
that use ModemManager.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%{_kf6_libdir}/libKF6ModemManagerQt.so
%{_kf6_libdir}/cmake/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-2
- Prepare for Oreon 11 (RP1)
