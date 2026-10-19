%global source0_hash 3b85c3929034b0a99da777130c34d99f006fcd3a9d56564159399a33fee0e504
%{?mingw_package_header}
%global pkgname qtkeychain
Name:           mingw-%{pkgname}
Version:        0.17.0
Release:        1%{?dist}
Summary:        MinGW Windows qtkeychain library
BuildArch:      noarch
License:        BSD-3-Clause
Url:            https://github.com/frankosterfeld/%{pkgname}
Source0:        https://github.com/frankosterfeld/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz
Patch0:         qtkeychain_include.patch
Patch1:         qtkeychain_cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qttools-tools
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qttools-tools
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake \
    -DBUILD_WITH_QT4:BOOL=OFF
%mingw_make_build
%install
%mingw_make_install
%find_lang %{pkgname} --with-qt
grep %{mingw32_datadir}/qt5keychain/translations %{pkgname}.lang > mingw32_%{pkgname}-qt5.lang
grep %{mingw64_datadir}/qt5keychain/translations %{pkgname}.lang > mingw64_%{pkgname}-qt5.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qtkeychain-qt5 -f %{oreon_filedir}/mingw32-qtkeychain-qt5.list
%files -n mingw64-qtkeychain-qt5 -f %{oreon_filedir}/mingw64-qtkeychain-qt5.list

%changelog

%autochangelog
