%global source0_hash b43c7cb765109a91ad9ef7d5856c4584b380349837baf63ccca4b45a67925ab5

%global stable_kf6 stable


%define         base_name milou


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-%{base_name}
Version:        6.7.5
Release: 1%{?dist}
Summary: A dedicated KDE search application built on top of Baloo

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}.git

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KirigamiPlatform)

# Qt
BuildRequires:  qt6-qtbase-devel

# Plasma
BuildRequires:  cmake(Plasma)

Requires:       kf6-filesystem

Obsoletes:      kde-plasma-milou < 5.0.0
Provides:       kde-plasma-milou = %{version}-%{release}

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang milou --with-qt --all-name


%files -f milou.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/milou/
%{_kf6_qtplugindir}/plasma/applets/org.kde.milou.so


%changelog
%autochangelog
