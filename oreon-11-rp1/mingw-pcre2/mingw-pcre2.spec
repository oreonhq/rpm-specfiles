%global source0_hash 15fbc5aba6beee0b17aecb04602ae39432393aba1ebd8e39b7cabf7db883299f
%{?mingw_package_header}
%global pkgname pcre2
Name:          mingw-%{pkgname}
Version:       10.46
Release:        1%{?dist}
Summary:        MinGW Windows pcre2 library
License:       BSD-3-Clause
URL:           http://www.pcre.org/
Source0:        https://github.com/PhilipHazel/pcre2/releases/download/pcre2-%{version}/pcre2-%{version}.tar.bz2
Patch0:        pcre2-10.10-Fix-multilib.patch
Patch100:      pcre2-10.23-mingw.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
find %{buildroot} -name "*.la" -delete
chmod 0644 %{buildroot}%{mingw32_libdir}/*.dll.a
chmod 0644 %{buildroot}%{mingw64_libdir}/*.dll.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-pcre2 -f %{oreon_filedir}/mingw32-pcre2.list
%files -n mingw32-pcre2-static -f %{oreon_filedir}/mingw32-pcre2-static.list
%files -n mingw64-pcre2 -f %{oreon_filedir}/mingw64-pcre2.list
%files -n mingw64-pcre2-static -f %{oreon_filedir}/mingw64-pcre2-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.46-2
- Prepare for Oreon 11 (RP1)
