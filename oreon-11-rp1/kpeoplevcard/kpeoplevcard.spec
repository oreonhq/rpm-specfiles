%global source0_hash 8de5df5a3abeed2b13fc56f33d1846ae5b90adfc2127bc1b0ffa5e300b7663c3
Name:           kpeoplevcard
Version:        0.1
Release:        9%{?dist}
Summary:        Expose VCard contacts to KPeople
License:        LGPLv2+
URL:            https://invent.kde.org/pim/kpeoplevcard
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  kf5-rpm-macros
# /oreon:deps
%description
Kpeoplevcard provides a datasource plugin for KPeople that reads vCard files
from the local filesystem.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kpeoplevcard-devel -f %{oreon_filedir}/kpeoplevcard-devel.list

%changelog

%autochangelog
