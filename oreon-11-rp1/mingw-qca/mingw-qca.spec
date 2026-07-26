%global source0_hash 1c5b722da93d559365719226bb121c726ec3c0dc4c67dea34f1e50e4e0d14a02

%{?mingw_package_header}

%global pkgname qca

Name:           mingw-%{pkgname}
Version:        2.3.10
Release:        3%{?dist}
Summary:        MinGW Windows Qt Cryptographic Architecture
BuildArch:      noarch

License:        LGPL-2.0-or-later
URL:            https://userbase.kde.org/QCA
Source0:        http://download.kde.org/stable/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.xz
# Install pkgconfig file
Patch0:         qca_pkgconfig.patch

BuildRequires:  make
BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-qt5-qtbase
# TODO
# BuildRequires:  mingw32-botan2
# BuildRequires:  mingw32-pkcs11-helper
# BuildRequires:  mingw32-nss
# BuildRequires:  mingw32-cyrus-sasl

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-qt5-qtbase
# TODO
# BuildRequires:  mingw64-botan2
# BuildRequires:  mingw64-pkcs11-helper
# BuildRequires:  mingw64-nss
# BuildRequires:  mingw64-cyrus-sasl

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

# Drop man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libqca-qt5.dll
%{mingw32_bindir}/mozcerts-qt5.exe
%{mingw32_bindir}/qcatool-qt5.exe
%{mingw32_prefix}/certs/
%{mingw32_includedir}/qt5/QtCrypto
%{mingw32_libdir}/libqca-qt5.dll.a
%dir %{mingw32_libdir}/qt5/plugins/crypto/
%{mingw32_libdir}/qt5/plugins/crypto/libqca-gcrypt.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-gnupg.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-logger.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-ossl.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-softstore.dll
%{mingw32_libdir}/cmake/Qca-qt5
%{mingw32_libdir}/pkgconfig/qca2-qt5.pc
%{mingw32_libdir}/qt5/mkspecs/features/crypto.prf

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libqca-qt5.dll
%{mingw64_bindir}/mozcerts-qt5.exe
%{mingw64_bindir}/qcatool-qt5.exe
%{mingw64_prefix}/certs/
%{mingw64_includedir}/qt5/QtCrypto
%{mingw64_libdir}/libqca-qt5.dll.a
%dir %{mingw64_libdir}/qt5/plugins/crypto/
%{mingw64_libdir}/qt5/plugins/crypto/libqca-gcrypt.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-gnupg.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-logger.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-ossl.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-softstore.dll
%{mingw64_libdir}/cmake/Qca-qt5
%{mingw64_libdir}/pkgconfig/qca2-qt5.pc
%{mingw64_libdir}/qt5/mkspecs/features/crypto.prf

%changelog
%autochangelog
