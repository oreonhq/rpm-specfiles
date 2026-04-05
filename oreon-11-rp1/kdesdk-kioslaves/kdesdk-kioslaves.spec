%undefine __cmake_in_source_build
%global base_name kdesdk-kio

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdesdk-kioslaves
Summary: KDESDK KIOslaves
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-kio-%{version}.tar.xz

BuildRequires: perl-generators

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)

# translations moved here
Conflicts: kde-l10n < 17.03

Conflicts:      kdesdk-common < 4.10.80
Provides:       kdesdk-kioslave = %{version}-%{release}
Obsoletes:      kdesdk-kioslave < 4.10.80

Provides: kio5-perldoc = %{version}-%{release}

%description
KDE SDK kioslaves:
* perldoc KIOSlave


%prep
%autosetup -p1 -n %{base_name}-%{version}


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{base_name} --all-name


%files -f %{base_name}.lang
%{_kf6_plugindir}/kio/perldoc.so
%{_kf6_datadir}/kio_perldoc/


%changelog	
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
