%global source0_hash 4d312b811bdee7016f6273df8c355f7ed89b60aa0c88eba666a880d997b140f4

%global stable_kf6 stable


Name:           kdevelop-php
Summary:        Php language and documentation plugins for KDevelop
Version:        26.08.0
Release:        1%{?dist}

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
BuildRequires:  kdevelop-devel = 9:%{version}

%{?kdevelop_requires}

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n kdev-php-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

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
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
