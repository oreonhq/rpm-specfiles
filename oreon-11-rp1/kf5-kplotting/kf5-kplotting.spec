%undefine __cmake_in_source_build
%global framework kplotting

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon for plotting

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  pcre-devel
BuildRequires:  perl-interpreter

BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5UiPlugin)

Requires:       kf5-filesystem >= %{majmin}

%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Plotting.so.*
%{_kf5_qtplugindir}/designer/kplotting5widgets.so

%files devel

%{_kf5_includedir}/KPlotting/
%{_kf5_libdir}/libKF5Plotting.so
%{_kf5_libdir}/cmake/KF5Plotting/
%{_kf5_archdatadir}/mkspecs/modules/qt_KPlotting.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
