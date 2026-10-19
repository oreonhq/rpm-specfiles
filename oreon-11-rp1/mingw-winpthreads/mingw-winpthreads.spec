%global source0_hash 5afe822af5c4edbf67daaf45eec61d538f49eef6b19524de64897c6b95828caf
%global mingw_build_ucrt64 1
%{?mingw_package_header}
%global enable_tests 0
Name:           mingw-winpthreads
Version:        13.0.0
Release:        1%{?dist}
Summary:        MinGW pthread library
License:        BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            http://mingw-w64.sourceforge.net/
Source0:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
BuildArch:      noarch
%if 0%{?enable_tests}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-crt
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-crt
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  ucrt64-crt
BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc-c++
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mingw-w64-v%{version}%{?pre:-%{pre}}

%build

pushd mingw-w64-libraries/winpthreads
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
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-winpthreads usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-winpthreads-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-winpthreads usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-winpthreads-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-winpthreads usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-winpthreads-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?enable_tests}
%check

export WINEPREFIX=/tmp/wine-winpthreads
mkdir $WINEPREFIX
winecfg || :
pushd mingw-w64-libraries/winpthreads
    %mingw_make check -k || :
popd
wineserver --kill || :
rm -rf /tmp/wine-winpthreads
%endif
%files -f %{oreon_filedir}/main.list
%files -n mingw32-winpthreads -f %{oreon_filedir}/mingw32-winpthreads.list
%files -n mingw32-winpthreads-static -f %{oreon_filedir}/mingw32-winpthreads-static.list
%files -n mingw64-winpthreads -f %{oreon_filedir}/mingw64-winpthreads.list
%files -n mingw64-winpthreads-static -f %{oreon_filedir}/mingw64-winpthreads-static.list
%files -n ucrt64-winpthreads -f %{oreon_filedir}/ucrt64-winpthreads.list
%files -n ucrt64-winpthreads-static -f %{oreon_filedir}/ucrt64-winpthreads-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-3
- Prepare for Oreon 11 (RP1)
