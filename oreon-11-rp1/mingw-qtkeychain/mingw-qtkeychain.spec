%global source0_hash f4254dc8f0933b06d90672d683eab08ef770acd8336e44dfa030ce041dc2ca22

%{?mingw_package_header}

%global pkgname qtkeychain

Name:           mingw-%{pkgname}
Version:        0.15.0
Release:        2%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        BSD-3-Clause
Url:            https://github.com/frankosterfeld/%{pkgname}
Source0:        https://github.com/frankosterfeld/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Add missing cmath include
Patch0:         qtkeychain_include.patch
# Don't add /utf-8 when building with mingw
Patch1:         qtkeychain_cmake.patch

BuildRequires:  make
BuildRequires:  cmake

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

%files -n mingw32-%{pkgname}-qt5 -f mingw32_%{pkgname}-qt5.lang
%license COPYING
%{mingw32_bindir}/libqt5keychain.dll
%{mingw32_includedir}/qt5keychain/
%{mingw32_libdir}/libqt5keychain.dll.a
%{mingw32_libdir}/cmake/Qt5Keychain
%{mingw32_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files -n mingw64-%{pkgname}-qt5 -f mingw64_%{pkgname}-qt5.lang
%license COPYING
%{mingw64_bindir}/libqt5keychain.dll
%{mingw64_includedir}/qt5keychain/
%{mingw64_libdir}/libqt5keychain.dll.a
%{mingw64_libdir}/cmake/Qt5Keychain
%{mingw64_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%changelog
%autochangelog
