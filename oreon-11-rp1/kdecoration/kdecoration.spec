%global source1_hash c9b1094ab02591ab2bc1ed1f4ac58094822df909799489456a8ca30c6be9f277
%global source0_hash 7ff1fe2854ca08a21a1ba47f1b0c97d12ea24f1db618631319cba4023ca53d86
%global stable_kf6 stable
Name:    kdecoration
Summary:        A plugin-based library to create window decorations
Version:        6.7.5
Release:        1%{?dist}
License: LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0
URL:     https://invent.kde.org/plasma/kdecoration
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_kf6_qtplugindir}/org.kde.kdecoration2/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kdecoration-devel -f %{oreon_filedir}/kdecoration-devel.list

%changelog

%autochangelog
