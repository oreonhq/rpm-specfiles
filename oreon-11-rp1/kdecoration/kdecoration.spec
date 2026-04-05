%global stable_kf6 stable

Name:    kdecoration
Summary: A plugin-based library to create window decorations
Version: 6.6.2
Release:	2%{?dist}

License: LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0
URL:     https://invent.kde.org/plasma/kdecoration

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

# For AutoReq cmake-filesystem
BuildRequires: cmake
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: make

Requires:       kf6-filesystem

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# create/own plugin dir
mkdir -p %{buildroot}%{_kf6_qtplugindir}/org.kde.kdecoration2/

%files
%license LICENSES/*.txt
%{_kf6_libdir}/libkdecorations3.so.6
%{_kf6_libdir}/libkdecorations3.so.%{version}
%{_kf6_libdir}/libkdecorations3private.so.2
%{_kf6_libdir}/libkdecorations3private.so.%{version}
%{_datadir}/locale/*/LC_MESSAGES/kdecoration.mo

%files devel
%{_kf6_libdir}/libkdecorations3.so
%{_kf6_libdir}/libkdecorations3private.so
%{_kf6_libdir}/cmake/KDecoration3/
%{_kf6_includedir}/kdecoration3_version.h
%{_includedir}/KDecoration3

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
