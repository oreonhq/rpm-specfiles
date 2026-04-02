%global framework kauth

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 module to perform actions as privileged user
# LGPL-2.0-or-later is also in the project's LICENSES, but is unused according to reuse.
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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

%find_lang_kf6 kauth6_qt

%files -f kauth6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_kf6_datadir}/kf6/kauth/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6AuthCore.so.6
%{_kf6_libdir}/libKF6AuthCore.so.%{version}
%{_kf6_qtplugindir}/kf6/kauth/

%files devel
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/cmake/KF6Auth/
%{_kf6_libdir}/libKF6AuthCore.so
%{_kf6_libexecdir}/kauth/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
