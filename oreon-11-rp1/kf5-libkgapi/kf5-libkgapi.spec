%global source0_hash 10249f32a3a8a26a73e251d0415d42b69827ad354b451f62bdbb01bc6a40d7a3
%global srcname libkgapi
%global _changelog_trimtime %(date +%s -d "1 year ago")
%global _lto_cflags %{nil}
Name:    kf5-libkgapi
Version: 23.08.5
Release:        1%{?dist}
Summary:        Library to access to Google services
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/pim/%{srcname}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{srcname}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtxmlpatterns-devel
# /oreon:deps
%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kcalendarcore-devel
Requires:       kf5-kcontacts-devel
%description devel
Libraries and header files for developing applications that use akonadi-google
resources.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

find ./poqm -type f -execdir mv {} libkgapi_qt5.po \;
sed -i "/ecm_create_qm_loader/ s/libkgapi_qt/libkgapi_qt5/" src/core/CMakeLists.txt
sed -i "/EXTRACT_TR_STRINGS/ s/libkgapi_qt/libkgapi_qt5/" Messages.sh
%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang_kf5 libkgapi_qt5
rm %{buildroot}%{_libdir}/sasl2/libkdexoauth2.so*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
