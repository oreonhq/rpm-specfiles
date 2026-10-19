%global stable_kf6 stable
%global source0_hash e7b7f90aa23ee5b2b5943003a376f96fa75591716cb7d99a22b5ef08020fa519
Name:    kdeedu-data
Summary:        Shared icons, artwork and data files for educational applications
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-only
URL:     https://invent.kde.org/education/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildArch: noarch
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kde-filesystem
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

