# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6eaf921d9eb987d3820b364ea9775bc19b965ec81490b6fdd716526c28e1995c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global mingw_build_ucrt64 1

%{?mingw_package_header}


Name:           mingw-crt
Version:        14.0.0
Release:        1%{?dist}
Summary:        MinGW Windows cross-compiler runtime

License:        LicenseRef-Oreon-Public-Domain AND ZPL-2.1
URL:            https://www.mingw-w64.org/
Source0:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
Source4:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2.sig
Source5:        mingw-w64-key.asc


Source1:       standard-dlls-mingw32
Source2:       standard-dlls-mingw64
Source3:       standard-dlls-ucrt64

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gnupg2

BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-gcc

BuildRequires:  ucrt64-filesystem >= 133
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-headers
BuildRequires:  ucrt64-gcc

%description
MinGW Windows cross-compiler runtime, base libraries.


%package -n mingw32-crt
Summary:        MinGW Windows cross-compiler runtime for the win32 target
Requires:       mingw32-filesystem >= 133
Provides:       %(sed "s/\(.*\)/mingw32(\1) /g" %{SOURCE1} | tr "\n" " ")
Provides:       mingw32(mscoree.dll)

%description -n mingw32-crt
MinGW Windows cross-compiler runtime, base libraries for the win32 target.

%package -n mingw64-crt
Summary:        MinGW Windows cross-compiler runtime for the win64 target
Requires:       mingw64-filesystem >= 133
Provides:       %(sed "s/\(.*\)/mingw64(\1) /g" %{SOURCE2} | tr "\n" " ")
Provides:       mingw64(mscoree.dll)

%description -n mingw64-crt
MinGW Windows cross-compiler runtime, base libraries for the win64 target.

%package -n ucrt64-crt
Summary:        MinGW Windows cross-compiler runtime for the win64 target
Requires:       ucrt64-filesystem >= 133
Provides:       %(sed "s/\(.*\)/ucrt64(\1) /g" %{SOURCE3} | tr "\n" " ")
Provides:       ucrt64(mscoree.dll)

%description -n ucrt64-crt
MinGW Windows cross-compiler runtime, base libraries for the win64 target.


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE5} --sig %{SOURCE4} --data %{SOURCE0}
%autosetup -p1 -n mingw-w64-v%{version}


%build
pushd mingw-w64-crt
    # Filter out -fstack-protector and -lssp from LDFLAGS as libssp is not yet potentially built with the bootstrap gcc
    MINGW32_LDFLAGS="`echo %{mingw32_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW64_LDFLAGS="`echo %{mingw64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    UCRT64_LDFLAGS="`echo %{ucrt64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW32_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
    MINGW64_CONFIGURE_ARGS="--disable-lib32 --with-default-msvcrt=msvcrt"
    UCRT64_CONFIGURE_ARGS="--disable-lib32 --with-default-msvcrt=ucrt"
    %mingw_configure
    %mingw_make_build
popd


%install
pushd mingw-w64-crt
    %mingw_make_install
popd

rm -rf %{buildroot}%{mingw32_includedir}/*.c
rm -rf %{buildroot}%{mingw64_includedir}/*.c
rm -rf %{buildroot}%{ucrt64_includedir}/*.c


%files -n mingw32-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw32_libdir}/*

%files -n mingw64-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw64_libdir}/*

%files -n ucrt64-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{ucrt64_libdir}/*

%changelog
%autochangelog
