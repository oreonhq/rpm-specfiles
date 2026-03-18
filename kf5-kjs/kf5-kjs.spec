%global framework kjs

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 3 functional module with JavaScript interpreter

# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  pcre-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 1 Tier 1 functional module with JavaScript interpret.

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
%cmake_kf5

%cmake_build


%install
%cmake_install

chmod +x %{buildroot}%{_kf5_datadir}/kf5/kjs/create_hash_table

%find_lang %{name} --with-man --all-name


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license COPYING.LIB
%{_kf5_bindir}/kjs5
%{_kf5_libdir}/libKF5JS.so.*
%{_kf5_libdir}/libKF5JSApi.so.*
%{_mandir}/man1/kjs5.1*

%files devel
%dir %{_kf5_datadir}/kf5/kjs/
%{_kf5_datadir}/kf5/kjs/create_hash_table
%{_kf5_includedir}/kjs_version.h
%{_kf5_includedir}/kjs/
%{_kf5_includedir}/wtf/
%{_kf5_libdir}/libKF5JS.so
%{_kf5_libdir}/libKF5JSApi.so
%{_kf5_libdir}/cmake/KF5JS/
%{_kf5_archdatadir}/mkspecs/modules/qt_KJS.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KJSApi.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-6
- Prepare for Oreon 11 (RP1)
