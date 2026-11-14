# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6eaf921d9eb987d3820b364ea9775bc19b965ec81490b6fdd716526c28e1995c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global mingw_build_ucrt64 1
%{?mingw_package_header}

%global enable_tests 0

Name:           mingw-winpthreads
Version:        14.0.0
Release:        2%{?dist}
Summary:        MinGW pthread library

License:        BSD-3-Clause AND MIT AND LicenseRef-Oreon-Public-Domain
URL:            https://www.mingw-w64.org/
Source0:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2
Source4:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2.sig
Source5:        mingw-w64-key.asc
Patch0:         clear_tls.patch

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  ucrt64-filesystem >= 133
%if %{without bootstrap}
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-crt
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-crt
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-crt
%endif

%if 0%{?enable_tests}
BuildRequires:  wine-wow
%endif


%description
The POSIX 1003.1-2001 standard defines an application programming
interface (API) for writing multithreaded applications. This interface
is known more commonly as pthreads. A good number of modern operating
systems include a threading library of some kind: Solaris (UI)
threads, Win32 threads, DCE threads, DECthreads, or any of the draft
revisions of the pthreads standard. The trend is that most of these
systems are slowly adopting the pthreads standard API, with
application developers following suit to reduce porting woes.

Win32 does not, and is unlikely to ever, support pthreads
natively. This project seeks to provide a freely available and
high-quality solution to this problem.


# Win32
%package -n mingw32-winpthreads
Summary:        MinGW pthread library for the win32 target

%description -n mingw32-winpthreads
The POSIX 1003.1-2001 standard defines an application programming
interface (API) for writing multithreaded applications. This interface
is known more commonly as pthreads. A good number of modern operating
systems include a threading library of some kind: Solaris (UI)
threads, Win32 threads, DCE threads, DECthreads, or any of the draft
revisions of the pthreads standard. The trend is that most of these
systems are slowly adopting the pthreads standard API, with
application developers following suit to reduce porting woes.

Win32 does not, and is unlikely to ever, support pthreads
natively. This project seeks to provide a freely available and
high-quality solution to this problem.

%if %{without bootstrap}
%package -n mingw32-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       mingw32-winpthreads = %{version}-%{release}

%description -n mingw32-winpthreads-static
Static version of the MinGW Windows pthreads library.
%endif


# Win64
%package -n mingw64-winpthreads
Summary:        MinGW pthread library for the win64 target
Obsoletes:      mingw64-pthreads < 2.8.0-25.20110511cvs

%description -n mingw64-winpthreads
The POSIX 1003.1-2001 standard defines an application programming
interface (API) for writing multithreaded applications. This interface
is known more commonly as pthreads. A good number of modern operating
systems include a threading library of some kind: Solaris (UI)
threads, Win32 threads, DCE threads, DECthreads, or any of the draft
revisions of the pthreads standard. The trend is that most of these
systems are slowly adopting the pthreads standard API, with
application developers following suit to reduce porting woes.

Win32 does not, and is unlikely to ever, support pthreads
natively. This project seeks to provide a freely available and
high-quality solution to this problem.

%if %{without bootstrap}
%package -n mingw64-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       mingw64-winpthreads = %{version}-%{release}

%description -n mingw64-winpthreads-static
Static version of the MinGW Windows pthreads library.
%endif


%package -n ucrt64-winpthreads
Summary:        MinGW pthread library for the win64 target

%description -n ucrt64-winpthreads
The POSIX 1003.1-2001 standard defines an application programming
interface (API) for writing multithreaded applications. This interface
is known more commonly as pthreads. A good number of modern operating
systems include a threading library of some kind: Solaris (UI)
threads, Win32 threads, DCE threads, DECthreads, or any of the draft
revisions of the pthreads standard. The trend is that most of these
systems are slowly adopting the pthreads standard API, with
application developers following suit to reduce porting woes.

Win32 does not, and is unlikely to ever, support pthreads
natively. This project seeks to provide a freely available and
high-quality solution to this problem.

%if %{without bootstrap}
%package -n ucrt64-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       ucrt64-winpthreads = %{version}-%{release}

%description -n ucrt64-winpthreads-static
Static version of the MinGW Windows pthreads library.
%endif

%{?mingw_debug_package}


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE5} --sig %{SOURCE4} --data %{SOURCE0}
%autosetup -p1 -n mingw-w64-v%{version}%{?pre:-%{pre}}


%build
%if %{with bootstrap}
# headers only so mingw-headers can install before the cross gcc exists
:
%else
pushd mingw-w64-libraries/winpthreads
    MINGW32_LDFLAGS="`echo %{mingw32_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW64_LDFLAGS="`echo %{mingw64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    UCRT64_LDFLAGS="`echo %{ucrt64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    %mingw_configure
    %mingw_make_build
popd
%endif


%install
%if %{with bootstrap}
for root in %{mingw32_includedir} %{mingw64_includedir} %{ucrt64_includedir}; do
  mkdir -p %{buildroot}$root
  cp -a mingw-w64-libraries/winpthreads/include/. %{buildroot}$root/
done
%else
pushd mingw-w64-libraries/winpthreads
    %mingw_make_install
popd
find %{buildroot} -name "*.la" -delete
%endif


%if 0%{?enable_tests}
%if %{without bootstrap}
%check
export WINEPREFIX=/tmp/wine-winpthreads
mkdir $WINEPREFIX
winecfg
pushd mingw-w64-libraries/winpthreads
    %mingw_make check -k
popd
wineserver --kill
rm -rf /tmp/wine-winpthreads
%endif
%endif


# Win32
%files -n mingw32-winpthreads
%license COPYING
%if %{without bootstrap}
%{mingw32_bindir}/libwinpthread-1.dll
%{mingw32_libdir}/libwinpthread.dll.a
%{mingw32_libdir}/libpthread.dll.a
%endif
%{mingw32_includedir}/pthread.h
%{mingw32_includedir}/pthread_compat.h
%{mingw32_includedir}/pthread_signal.h
%{mingw32_includedir}/pthread_time.h
%{mingw32_includedir}/pthread_unistd.h
%{mingw32_includedir}/sched.h
%{mingw32_includedir}/semaphore.h

%if %{without bootstrap}
%files -n mingw32-winpthreads-static
%{mingw32_libdir}/libwinpthread.a
%{mingw32_libdir}/libpthread.a
%endif

# Win64
%files -n mingw64-winpthreads
%license COPYING
%if %{without bootstrap}
%{mingw64_bindir}/libwinpthread-1.dll
%{mingw64_libdir}/libwinpthread.dll.a
%{mingw64_libdir}/libpthread.dll.a
%endif
%{mingw64_includedir}/pthread.h
%{mingw64_includedir}/pthread_compat.h
%{mingw64_includedir}/pthread_signal.h
%{mingw64_includedir}/pthread_time.h
%{mingw64_includedir}/pthread_unistd.h
%{mingw64_includedir}/sched.h
%{mingw64_includedir}/semaphore.h

%if %{without bootstrap}
%files -n mingw64-winpthreads-static
%{mingw64_libdir}/libwinpthread.a
%{mingw64_libdir}/libpthread.a
%endif

# ucrt64
%files -n ucrt64-winpthreads
%license COPYING
%if %{without bootstrap}
%{ucrt64_bindir}/libwinpthread-1.dll
%{ucrt64_libdir}/libwinpthread.dll.a
%{ucrt64_libdir}/libpthread.dll.a
%endif
%{ucrt64_includedir}/pthread.h
%{ucrt64_includedir}/pthread_compat.h
%{ucrt64_includedir}/pthread_signal.h
%{ucrt64_includedir}/pthread_time.h
%{ucrt64_includedir}/pthread_unistd.h
%{ucrt64_includedir}/sched.h
%{ucrt64_includedir}/semaphore.h

%if %{without bootstrap}
%files -n ucrt64-winpthreads-static
%{ucrt64_libdir}/libwinpthread.a
%{ucrt64_libdir}/libpthread.a
%endif

%changelog
%autochangelog
