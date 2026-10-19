%global stable_kf6 stable
%global source0_hash ddcb77d5832070ab5f07bbfc15f404b030e67e06f60d1bb3be8ce8af5f413fdd
Name:           khealthcertificate
Version:        25.12.3
Release:        1%{?dist}
License:        W3C-20150513 AND LGPL-2.0-or-later AND BSD-3-Clause AND CC0-1.0 AND MIT AND Apache-2.0
Summary:        Handling of digital vaccination, test and recovery certificates.
Url:            https://invent.kde.org/pim/khealthcertificate
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package devel
Summary: Development files for khealthcertificate
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%files -f %{oreon_filedir}/main.list
%files -n khealthcertificate-devel -f %{oreon_filedir}/khealthcertificate-devel.list

%changelog

%autochangelog
