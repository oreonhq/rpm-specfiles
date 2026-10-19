%global stable_kf6 stable
%global source0_hash f40957124b78a7dd954016bffa238c9ef2bb16a30a09e35f85cca35d3053547c
Name:    poxml
Summary:        Text utilities from kdesdk
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/sdk/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
Text utilities from kdesdk, including
po2xml
split2po
swappo
xml2pot

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
