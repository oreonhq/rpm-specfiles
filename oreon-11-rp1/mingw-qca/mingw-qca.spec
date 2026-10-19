%global source0_hash 1c5b722da93d559365719226bb121c726ec3c0dc4c67dea34f1e50e4e0d14a02
%{?mingw_package_header}
%global pkgname qca
Name:           mingw-%{pkgname}
Version:        2.3.10
Release:        1%{?dist}
Summary:        MinGW Windows Qt Cryptographic Architecture
BuildArch:      noarch
License:        LGPL-2.0-or-later
URL:            https://userbase.kde.org/QCA
Source0:        http://download.kde.org/stable/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.xz
Patch0:         qca_pkgconfig.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-qt5-qtbase
# /oreon:deps
%description
MinGW Windows Qt Cryptographic Architecture.

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Qt Cryptographic Architecture
%description -n mingw32-%{pkgname}-qt5
MinGW Windows Qt Cryptographic Architecture.

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Qt Cryptographic Architecture
%description -n mingw64-%{pkgname}-qt5
MinGW Windows Qt Cryptographic Architecture.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

export MINGW32_CMAKE_ARGS="
    -DQCA_FEATURE_INSTALL_DIR:PATH=%{mingw32_libdir}/qt5/mkspecs/features
    -DQCA_INCLUDE_INSTALL_DIR:PATH=%{mingw32_includedir}/qt5
    -DQCA_LIBRARY_INSTALL_DIR:PATH=%{mingw32_libdir}
    -DQCA_PLUGINS_INSTALL_DIR:PATH=%{mingw32_libdir}/qt5/plugins
    -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{mingw32_includedir}/qt5
"
export MINGW64_CMAKE_ARGS="
    -DQCA_FEATURE_INSTALL_DIR:PATH=%{mingw64_libdir}/qt5/mkspecs/features
    -DQCA_INCLUDE_INSTALL_DIR:PATH=%{mingw64_includedir}/qt5
    -DQCA_LIBRARY_INSTALL_DIR:PATH=%{mingw64_libdir}
    -DQCA_PLUGINS_INSTALL_DIR:PATH=%{mingw64_libdir}/qt5/plugins
    -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{mingw64_includedir}/qt5
"
%mingw_cmake \
    -DUSE_RELATIVE_PATHS=ON \
    -DQT4_BUILD:BOOL=OFF
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qca-qt5 -f %{oreon_filedir}/mingw32-qca-qt5.list
%files -n mingw64-qca-qt5 -f %{oreon_filedir}/mingw64-qca-qt5.list

%changelog

%autochangelog
