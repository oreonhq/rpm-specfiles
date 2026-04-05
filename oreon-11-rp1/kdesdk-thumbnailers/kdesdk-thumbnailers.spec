
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdesdk-thumbnailers
Summary: Thumbnailers for KDE
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/sdk/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  gettext-devel

# translations moved here
Conflicts: kde-l10n < 17.03

Conflicts:      kdesdk-common < 4.10.80
Obsoletes:      kde-thumbnailer-po <= 2.0
Obsoletes:      kdesdk-thumbnailers < 4.10.80
Provides:       kdesdk-thumbnailers = %{version}-%{release}
Provides:       kde-thumbnailer-po = %{version}-%{release}


%description
Thumbnailers for KDE, including gnu gettext po translation files and
gettext translation templates


%prep
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license LICENSES/*
%dir %{_qt6_plugindir}/kf6/thumbcreator
%{_qt6_plugindir}/kf6/thumbcreator/pothumbnail.so

%changelog	
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
