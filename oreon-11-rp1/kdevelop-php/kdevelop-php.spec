%global stable_kf6 stable

Name:           kdevelop-php
Summary:        Php language and documentation plugins for KDevelop
Version:        25.12.3
Release:	2%{?dist}

# Most files LGPLv2+/GPLv2+
License:        GPL-2.0-or-later
URL:            https://kdevelop.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/kdev-php-%{version}.tar.xz

# kdevelop depends on qt6-qtwebengine, which is only available on some arches
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)

BuildRequires:  cmake(KDevPlatform) >= 6.0
BuildRequires:  cmake(KDevelop-PG-Qt) >= 2.3.0
# Exact 9:%%{version} breaks dnf builddep when kdevelop-devel has another epoch/NVR in the repo
BuildRequires:  kdevelop-devel >= %{version}

%{?kdevelop_requires}

%description
%{summary}.


%prep
%setup -q -n kdev-php-%{version}


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# TODO Enable translations in stable build
%find_lang %{name} --all-name


%files -f %{name}.lang
%doc AUTHORS
%license LICENSES/*
%{_datadir}/kdevappwizard/
%{_datadir}/kdevphpsupport/
%{_includedir}/kdev-php/*
%{_libdir}/libkdevphp*.so
%{_libdir}/cmake/KDevPHP/*.cmake
%{_kf6_qtplugindir}/kdevplatform/
%{_datadir}/qlogging-categories6/kdevphpsupport.categories
%{_kf6_metainfodir}/org.kde.kdev-php.metainfo.xml


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Relax kdevelop-devel BuildRequires to >= %%{version} for dnf builddep

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
