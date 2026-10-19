%global source0_hash abb335114ff5b838329e11a0b6abf15e90198ff57b5853174ba4fc71f93e7966
%global srcname lxqt_wallet
Name:           %(echo %{srcname} |tr _ - )
Version:        4.1.0
Release:        1%{?dist}
Summary:        Create a kwallet like functionality for LXQt
License:        BSD-2-Clause
URL:            https://github.com/lxqt/%{srcname}
Source0:        https://github.com/lxqt/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  qt6-linguist
# /oreon:deps
%description
This project seeks to give a functionality for secure storage
of information that can be presented in key-values pair like
user names-passwords pairs.

Currently the project can store the information in KDE's kwallet,
GNOME's secret service or in an internal system that use libgcrypt
as its cryptographic backend.

The internal secure storage system allows the functionality to
be provided without dependencies on KDE or GNOME libraries.

This project is designed to be used by other projects simply by
adding the source folder in the build system and start using it.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblxqt-devel%{?_isa}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{srcname}-%{version}
cp -p backend/README README-backend
cp -p frontend/README README-frontend

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-wallet-devel -f %{oreon_filedir}/lxqt-wallet-devel.list

%changelog

%autochangelog
