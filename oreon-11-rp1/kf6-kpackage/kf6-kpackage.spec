%global framework kpackage

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	5%{?dist}
Summary:        KDE Frameworks 6 Tier 2 library to load and install packages as plugins

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-karchive-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf6_datadir}/kpackage/

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Package.so.*
%{_kf6_qtplugindir}/kpackage/
%{_kf6_datadir}/kpackage/
%{_kf6_bindir}/kpackagetool6
%{_mandir}/man1/kpackagetool6.1*

%files devel
%{_kf6_includedir}/KPackage/
%{_kf6_libdir}/libKF6Package.so
%{_kf6_libdir}/cmake/KF6Package/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

