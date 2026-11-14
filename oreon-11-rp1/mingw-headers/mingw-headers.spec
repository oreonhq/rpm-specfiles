# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6eaf921d9eb987d3820b364ea9775bc19b965ec81490b6fdd716526c28e1995c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global mingw_build_ucrt64 1
%global bundle_dummy_pthread_headers %{?with_bootstrap:1}%{!?with_bootstrap:0}

Name:           mingw-headers
Version:        14.0.0
Release:        1%{?dist}
Summary:        Win32/Win64 header files

License:        BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND ZPL-2.1 AND MIT-Khronos-old AND LicenseRef-Oreon-Public-Domain
URL:            https://www.mingw-w64.org/
Source0:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2
Source1:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2.sig
Source2:        mingw-w64-key.asc

Patch0:         mingw-headers-no-widl.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gnupg2
BuildRequires: mingw32-filesystem
BuildRequires: mingw64-filesystem
BuildRequires: ucrt64-filesystem


%description
MinGW Windows cross-compiler Win32 and Win64 header files.


%package -n mingw32-headers
Summary:        MinGW Windows cross-compiler Win32 header files
Requires:       mingw32-filesystem
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       mingw32-winpthreads
%endif

%description -n mingw32-headers
MinGW Windows cross-compiler Win32 header files.

%package -n mingw64-headers
Summary:        MinGW Windows cross-compiler Win64 header files
Requires:       mingw64-filesystem
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       mingw64-winpthreads
%endif

%description -n mingw64-headers
MinGW Windows cross-compiler Win64 header files.

%package -n ucrt64-headers
Summary:        MinGW Windows cross-compiler Win64 header files
Requires:       ucrt64-filesystem
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       ucrt64-winpthreads
%endif

%description -n ucrt64-headers
MinGW Windows cross-compiler Win64 header files.


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n mingw-w64-v%{version}%{?pre:-%{pre}}


%build
export MINGW32_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
export MINGW64_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
export UCRT64_CONFIGURE_ARGS="--with-default-msvcrt=ucrt"

pushd mingw-w64-headers
    %mingw_configure --enable-sdk=all --enable-idl
popd


%install
pushd mingw-w64-headers
    %mingw_make_install
popd

%if 0%{?bundle_dummy_pthread_headers} == 0
rm -f %{buildroot}%{mingw32_includedir}/pthread_signal.h
rm -f %{buildroot}%{mingw32_includedir}/pthread_time.h
rm -f %{buildroot}%{mingw32_includedir}/pthread_unistd.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_signal.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_time.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_unistd.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_signal.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_time.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_unistd.h
%endif


%files -n mingw32-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw32_includedir}/*

%files -n mingw64-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw64_includedir}/*

%files -n ucrt64-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{ucrt64_includedir}/*

%changelog
%autochangelog
