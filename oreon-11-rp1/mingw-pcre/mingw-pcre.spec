%global source0_hash none

%?mingw_package_header

%global name1 pcre
# Is this a stable/testing release:
#%%global rcversion RC1

Name:		mingw-%{name1}
Version:	8.45
%global myversion %{version}%{?rcversion:-%rcversion}
Release:	10%{?dist}
Summary:	MinGW Windows pcre library

License:	BSD-3-Clause
URL:		http://www.pcre.org/
Source0:        https://github.com/PCRE2Project/pcre2/releases/download/pcre2-%{version}/pcre2-%{version}.tar.bz2
Source2:        https://ftp.pcre.org/pub/pcre/Public-Key

# Refused by upstream, bug #675477
Patch1:        pcre-8.32-refused_spelling_terminated.patch
# Fix recursion stack estimator, upstream bug #2173, refused by upstream
Patch2:        pcre-8.41-fix_stack_estimator.patch
# Link applications to PCRE-specific symbols when using POSIX API, bug #1667614,
# upstream bug 1830, partially borrowed from PCRE2, proposed to upstream,
# This amends ABI, application built with this patch cannot run with
# previous libpcreposix builds.
Patch3:        pcre-8.42-Declare-POSIX-regex-function-names-as-macros-to-PCRE.patch
# Fix reading an uninitialized memory when populating a name table,
# upstream bug #2661, proposed to the upstream
Patch4:        pcre-8.44-Inicialize-name-table-memory-region.patch
# Implement CET, bug #1909554, proposed to the upstream
# <https://lists.exim.org/lurker/message/20201220.222016.d8cd6d61.en.html>
Patch5:        pcre-8.44-JIT-compiler-update-for-Intel-CET.patch
Patch6:        pcre-8.44-Pass-mshstk-to-the-compiler-when-Intel-CET-is-enable.patch

BuildArch:	noarch

BuildRequires:  make
BuildRequires:  git
BuildRequires:	redhat-rpm-config
BuildRequires:  gnupg2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


# Win32
%package -n mingw32-pcre
Summary:	MinGW Windows pcre library
Requires:	pkgconfig

%description -n mingw32-pcre
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw32-pcre-static
Summary:       Static version of the mingw32-pcre library
Requires:      mingw32-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-pcre-static
Static version of the mingw32-pcre library.

# Win64
%package -n mingw64-pcre
Summary:        MinGW Windows pcre library
Requires:       pkgconfig

%description -n mingw64-pcre
Cross compiled Perl-compatible regular expression library for use with mingw64.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw64-pcre-static
Summary:       Static version of the mingw64-pcre library
Requires:      mingw64-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-pcre-static
Static version of the mingw64-pcre library.


%?mingw_debug_package


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git_am -n pcre-%{version}
autoreconf -vif


%build
%mingw_configure --enable-utf8 --enable-unicode-properties --enable-static --enable-pcre8 --enable-pcre16 --enable-pcre32
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man/*

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw32_bindir}/pcre-config
%{mingw32_bindir}/pcregrep.exe
%{mingw32_bindir}/pcretest.exe
%{mingw32_bindir}/libpcre-1.dll
%{mingw32_bindir}/libpcre16-0.dll
%{mingw32_bindir}/libpcre32-0.dll
%{mingw32_bindir}/libpcrecpp-0.dll
%{mingw32_bindir}/libpcreposix-0.dll
%{mingw32_libdir}/libpcre.dll.a
%{mingw32_libdir}/libpcre16.dll.a
%{mingw32_libdir}/libpcre32.dll.a
%{mingw32_libdir}/libpcrecpp.dll.a
%{mingw32_libdir}/libpcreposix.dll.a
%{mingw32_libdir}/pkgconfig/libpcre.pc
%{mingw32_libdir}/pkgconfig/libpcre16.pc
%{mingw32_libdir}/pkgconfig/libpcre32.pc
%{mingw32_libdir}/pkgconfig/libpcrecpp.pc
%{mingw32_libdir}/pkgconfig/libpcreposix.pc
%{mingw32_includedir}/pcre.h
%{mingw32_includedir}/pcre_scanner.h
%{mingw32_includedir}/pcre_stringpiece.h
%{mingw32_includedir}/pcrecpp.h
%{mingw32_includedir}/pcrecpparg.h
%{mingw32_includedir}/pcreposix.h

%files -n mingw32-pcre-static
%{mingw32_libdir}/libpcre.a
%{mingw32_libdir}/libpcre16.a
%{mingw32_libdir}/libpcre32.a
%{mingw32_libdir}/libpcrecpp.a
%{mingw32_libdir}/libpcreposix.a

# Win64
%files -n mingw64-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw64_bindir}/pcre-config
%{mingw64_bindir}/pcregrep.exe
%{mingw64_bindir}/pcretest.exe
%{mingw64_bindir}/libpcre-1.dll
%{mingw64_bindir}/libpcre16-0.dll
%{mingw64_bindir}/libpcre32-0.dll
%{mingw64_bindir}/libpcrecpp-0.dll
%{mingw64_bindir}/libpcreposix-0.dll
%{mingw64_libdir}/libpcre.dll.a
%{mingw64_libdir}/libpcre16.dll.a
%{mingw64_libdir}/libpcre32.dll.a
%{mingw64_libdir}/libpcrecpp.dll.a
%{mingw64_libdir}/libpcreposix.dll.a
%{mingw64_libdir}/pkgconfig/libpcre.pc
%{mingw64_libdir}/pkgconfig/libpcre16.pc
%{mingw64_libdir}/pkgconfig/libpcre32.pc
%{mingw64_libdir}/pkgconfig/libpcrecpp.pc
%{mingw64_libdir}/pkgconfig/libpcreposix.pc
%{mingw64_includedir}/pcre.h
%{mingw64_includedir}/pcre_scanner.h
%{mingw64_includedir}/pcre_stringpiece.h
%{mingw64_includedir}/pcrecpp.h
%{mingw64_includedir}/pcrecpparg.h
%{mingw64_includedir}/pcreposix.h

%files -n mingw64-pcre-static
%{mingw64_libdir}/libpcre.a
%{mingw64_libdir}/libpcre16.a
%{mingw64_libdir}/libpcre32.a
%{mingw64_libdir}/libpcrecpp.a
%{mingw64_libdir}/libpcreposix.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.45-10
- Import
