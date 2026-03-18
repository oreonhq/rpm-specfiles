%global mingw_build_ucrt64 1
%{?mingw_package_header}

# Run the testsuite
%global enable_tests 0

Name:           mingw-winpthreads
Version:        13.0.0
Release:        3%{?dist}
Summary:        MinGW pthread library

# The main license of winpthreads is MIT, but parts of this library
# are derived from the "Posix Threads library for Microsoft Windows"
# http://locklessinc.com/articles/pthreads_on_windows/
License:        BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            http://mingw-w64.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-crt

BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-crt

BuildRequires:  ucrt64-filesystem >= 133
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-crt

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


%package -n mingw32-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       mingw32-winpthreads = %{version}-%{release}

%description -n mingw32-winpthreads-static
Static version of the MinGW Windows pthreads library.


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


%package -n mingw64-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       mingw64-winpthreads = %{version}-%{release}

%description -n mingw64-winpthreads-static
Static version of the MinGW Windows pthreads library.


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


%package -n ucrt64-winpthreads-static
Summary:        Static version of the MinGW Windows pthreads library
Requires:       ucrt64-winpthreads = %{version}-%{release}

%description -n ucrt64-winpthreads-static
Static version of the MinGW Windows pthreads library.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n mingw-w64-v%{version}%{?pre:-%{pre}}


%build
pushd mingw-w64-libraries/winpthreads
    # Filter out -fstack-protector and -lssp from LDFLAGS as libssp is not yet potentially built with the bootstrap gcc
    MINGW32_LDFLAGS="`echo %{mingw32_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW64_LDFLAGS="`echo %{mingw64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    UCRT64_LDFLAGS="`echo %{ucrt64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    %mingw_configure
    %mingw_make_build
popd


%install
pushd mingw-w64-libraries/winpthreads
    %mingw_make_install
popd
# Drop all .la files
find %{buildroot} -name "*.la" -delete


%if 0%{?enable_tests}
%check
# Prepare a wine prefix
export WINEPREFIX=/tmp/wine-winpthreads
mkdir $WINEPREFIX
winecfg || :

# Run the tests
pushd mingw-w64-libraries/winpthreads
    %mingw_make check -k || :
popd

# Clean up the wine prefix
wineserver --kill || :
rm -rf /tmp/wine-winpthreads
%endif


# Win32
%files -n mingw32-winpthreads
%license COPYING
%{mingw32_bindir}/libwinpthread-1.dll
%{mingw32_libdir}/libwinpthread.dll.a
%{mingw32_libdir}/libpthread.dll.a
%{mingw32_includedir}/pthread.h
%{mingw32_includedir}/pthread_compat.h
%{mingw32_includedir}/pthread_signal.h
%{mingw32_includedir}/pthread_time.h
%{mingw32_includedir}/pthread_unistd.h
%{mingw32_includedir}/sched.h
%{mingw32_includedir}/semaphore.h

%files -n mingw32-winpthreads-static
%{mingw32_libdir}/libwinpthread.a
%{mingw32_libdir}/libpthread.a

# Win64
%files -n mingw64-winpthreads
%license COPYING
%{mingw64_bindir}/libwinpthread-1.dll
%{mingw64_libdir}/libwinpthread.dll.a
%{mingw64_libdir}/libpthread.dll.a
%{mingw64_includedir}/pthread.h
%{mingw64_includedir}/pthread_compat.h
%{mingw64_includedir}/pthread_signal.h
%{mingw64_includedir}/pthread_time.h
%{mingw64_includedir}/pthread_unistd.h
%{mingw64_includedir}/sched.h
%{mingw64_includedir}/semaphore.h

%files -n mingw64-winpthreads-static
%{mingw64_libdir}/libwinpthread.a
%{mingw64_libdir}/libpthread.a

# ucrt64
%files -n ucrt64-winpthreads
%license COPYING
%{ucrt64_bindir}/libwinpthread-1.dll
%{ucrt64_libdir}/libwinpthread.dll.a
%{ucrt64_libdir}/libpthread.dll.a
%{ucrt64_includedir}/pthread.h
%{ucrt64_includedir}/pthread_compat.h
%{ucrt64_includedir}/pthread_signal.h
%{ucrt64_includedir}/pthread_time.h
%{ucrt64_includedir}/pthread_unistd.h
%{ucrt64_includedir}/sched.h
%{ucrt64_includedir}/semaphore.h

%files -n ucrt64-winpthreads-static
%{ucrt64_libdir}/libwinpthread.a
%{ucrt64_libdir}/libpthread.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-3
- Prepare for Oreon 11 (RP1)
