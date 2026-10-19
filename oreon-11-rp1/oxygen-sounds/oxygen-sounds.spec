%global source1_hash e58b3c0fb5684e79d2029403fcce3b94cdc6f0a6d77d6c22b814b3a1bcbf8a9b
%global source0_hash 0cc5b60004d8feb8b1de032cb5d3c056c98f62a8713589b90b471e5943e31ad9
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:           oxygen-sounds
Version:        6.7.5
Release:        1%{?dist}
Summary:        The Oxygen Sound Theme
License:        LGPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0 AND BSD-2-Clause
URL:            https://invent.kde.org/plasma/oxygen-sounds
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Provides:       oxygen-sound-theme = %{version}-%{release}
Obsoletes:      oxygen-sound-theme <= 5.24.50
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake_kf6} -DBUILD_WITH_QT6=ON
%{cmake_build}
%install
%{cmake_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
