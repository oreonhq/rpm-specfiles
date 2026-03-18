%{?mingw_package_header}

%global pkgname pcre2

Name:          mingw-%{pkgname}
Version:       10.46
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD-3-Clause
URL:           http://www.pcre.org/
Source:        https://github.com/PhilipHazel/pcre2/releases/download/pcre2-%{version}/pcre2-%{version}.tar.bz2

## Patches taken from native package ##
# Do no set RPATH if libdir is not /usr/lib
Patch0:        pcre2-10.10-Fix-multilib.patch

## MinGW specific patches ##
# Fix implicitly defined functions due to overly relaxed platform detection in macros
Patch100:      pcre2-10.23-mingw.patch


BuildArch:     noarch

BuildRequires: make
BuildRequires: automake autoconf libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils


%description
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Because of multilib patch
libtoolize --copy --force
autoreconf -vif


%build
%mingw_configure \
    --enable-jit \
    --enable-pcre2grep-jit \
    --disable-bsr-anycrlf \
    --disable-coverage \
    --disable-ebcdic \
    --disable-fuzz-support \
    --disable-never-backslash-C \
    --enable-newline-is-lf \
    --enable-pcre2-8 \
    --enable-pcre2-16 \
    --enable-pcre2-32 \
    --enable-pcre2grep-callout \
    --enable-pcre2grep-jit \
    --disable-pcre2grep-libbz2 \
    --disable-pcre2grep-libz \
    --disable-pcre2test-libedit \
    --disable-rebuild-chartables \
    --enable-shared \
    --enable-stack-for-recursion \
    --enable-static \
    --enable-unicode \
    --disable-valgrind
%mingw_make_build


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_datadir}/doc/*
rm -rf %{buildroot}%{mingw64_datadir}/doc/*
rm -rf %{buildroot}%{mingw32_datadir}/man/*
rm -rf %{buildroot}%{mingw64_datadir}/man/*

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Fix spurious-executable-perm
chmod 0644 %{buildroot}%{mingw32_libdir}/*.dll.a
chmod 0644 %{buildroot}%{mingw64_libdir}/*.dll.a


# Win32
%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/pcre2grep.exe
%{mingw32_bindir}/pcre2test.exe
%{mingw32_bindir}/pcre2-config
%{mingw32_bindir}/libpcre2-8-0.dll
%{mingw32_bindir}/libpcre2-16-0.dll
%{mingw32_bindir}/libpcre2-32-0.dll
%{mingw32_bindir}/libpcre2-posix-3.dll
%{mingw32_libdir}/libpcre2-8.dll.a
%{mingw32_libdir}/libpcre2-16.dll.a
%{mingw32_libdir}/libpcre2-32.dll.a
%{mingw32_libdir}/libpcre2-posix.dll.a
%{mingw32_libdir}/pkgconfig/libpcre2-*.pc
%{mingw32_includedir}/pcre2.h
%{mingw32_includedir}/pcre2posix.h

%files -n mingw32-%{pkgname}-static
%license COPYING
%{mingw32_libdir}/libpcre2-8.a
%{mingw32_libdir}/libpcre2-16.a
%{mingw32_libdir}/libpcre2-32.a
%{mingw32_libdir}/libpcre2-posix.a

# Win64
%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/pcre2grep.exe
%{mingw64_bindir}/pcre2test.exe
%{mingw64_bindir}/pcre2-config
%{mingw64_bindir}/libpcre2-8-0.dll
%{mingw64_bindir}/libpcre2-16-0.dll
%{mingw64_bindir}/libpcre2-32-0.dll
%{mingw64_bindir}/libpcre2-posix-3.dll
%{mingw64_libdir}/libpcre2-8.dll.a
%{mingw64_libdir}/libpcre2-16.dll.a
%{mingw64_libdir}/libpcre2-32.dll.a
%{mingw64_libdir}/libpcre2-posix.dll.a
%{mingw64_libdir}/pkgconfig/libpcre2-*.pc
%{mingw64_includedir}/pcre2.h
%{mingw64_includedir}/pcre2posix.h

%files -n mingw64-%{pkgname}-static
%license COPYING
%{mingw64_libdir}/libpcre2-8.a
%{mingw64_libdir}/libpcre2-16.a
%{mingw64_libdir}/libpcre2-32.a
%{mingw64_libdir}/libpcre2-posix.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.46-2
- Prepare for Oreon 11 (RP1)
