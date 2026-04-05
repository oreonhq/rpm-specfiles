%define         base_name milou


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-%{base_name}
Version: 6.6.2
Release:	2%{?dist}
Summary: A dedicated KDE search application built on top of Baloo

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}.git

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
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
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang milou --with-qt --all-name


%files -f milou.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/milou/
%{_kf6_qtplugindir}/plasma/applets/org.kde.milou.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
