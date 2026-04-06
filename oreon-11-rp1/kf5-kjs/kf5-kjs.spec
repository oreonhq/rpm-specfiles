%global framework kjs

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 3 functional module with JavaScript interpreter

# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0:        http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_dl_majmin}
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
