%global source0_hash none

%global stable_kf6 stable


# 
ExcludeArch: %{ix86}

Name:           oxygen-sounds
Version:        6.6.5
Release:        1%{?dist}
Summary:        The Oxygen Sound Theme

License:        LGPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0 AND BSD-2-Clause
URL:            https://invent.kde.org/plasma/oxygen-sounds

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

Provides:       oxygen-sound-theme = %{version}-%{release}
Obsoletes:      oxygen-sound-theme <= 5.24.50

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildArch:      noarch

%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%{cmake_kf6} -DBUILD_WITH_QT6=ON
%{cmake_build}

%install
%{cmake_install}


%files
%license LICENSES/*.txt
%{_kf6_datadir}/sounds/Oxygen-*
%{_kf6_datadir}/sounds/oxygen/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
