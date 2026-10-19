%global source0_hash 4dae6fdcd2bb0bb6c37b5f97c33c2be954da743985369cddac3546e3218bffb8
%?mingw_package_header
%global name1 pcre
Name:		mingw-%{name1}
Version:	8.45
%global myversion %{version}%{?rcversion:-%rcversion}
Release:        1%{?dist}
Summary:        MinGW Windows pcre library
License:	BSD-3-Clause
URL:		http://www.pcre.org/
Source0:        https://ftp.exim.org/pub/%{name1}/%{name1}-%{version}.tar.bz2
Source2:        Public-Key
Patch1:        pcre-8.32-refused_spelling_terminated.patch
Patch2:        pcre-8.41-fix_stack_estimator.patch
Patch3:        pcre-8.42-Declare-POSIX-regex-function-names-as-macros-to-PCRE.patch
Patch4:        pcre-8.44-Inicialize-name-table-memory-region.patch
Patch5:        pcre-8.44-JIT-compiler-update-for-Intel-CET.patch
Patch6:        pcre-8.44-Pass-mshstk-to-the-compiler-when-Intel-CET-is-enable.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  redhat-rpm-config
# /oreon:deps
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
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-pcre usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-pcre-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pcre usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pcre-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-pcre -f %{oreon_filedir}/mingw32-pcre.list
%files -n mingw32-pcre-static -f %{oreon_filedir}/mingw32-pcre-static.list
%files -n mingw64-pcre -f %{oreon_filedir}/mingw64-pcre.list
%files -n mingw64-pcre-static -f %{oreon_filedir}/mingw64-pcre-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.45-10
- Import
