%global source0_hash c08ae2388ef333e8403e670ad70c0a11f1eed021fd88308d7e02f596fcd9dc16
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pcre2
Version: 10.47
Release: 1%{?dist}
Summary: Perl-compatible regular expression library
License: BSD-3-Clause
URL: https://github.com/PCRE2Project/pcre2
Source0: https://github.com/PCRE2Project/pcre2/releases/download/pcre2-%{version}/pcre2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
%endif

%description
PCRE2 is a library of functions to support regular expressions whose syntax and semantics are as close as possible to those of the Perl 5 language.

%package devel
Summary: Perl-compatible regular expression library
Requires: pcre2%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libpcre2-8)
Provides: pkgconfig(libpcre2-16)
Provides: pkgconfig(libpcre2-32)
Provides: pkgconfig(libpcre2-posix)

%description devel
PCRE2 is a library of functions to support regular expressions whose syntax and semantics are as close as possible to those of the Perl 5 language.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --enable-pcre2-16 --enable-pcre2-32 --enable-pcre2grep-libz --enable-pcre2grep-libbz2
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}

%files
%license LICENCE.md
%{_bindir}/pcre2grep
%{_bindir}/pcre2test
%{_libdir}/libpcre2-8.so.0
%{_libdir}/libpcre2-8.so.0.*
%{_libdir}/libpcre2-16.so.0
%{_libdir}/libpcre2-16.so.0.*
%{_libdir}/libpcre2-32.so.0
%{_libdir}/libpcre2-32.so.0.*
%{_libdir}/libpcre2-posix.so.3
%{_libdir}/libpcre2-posix.so.3.*
%{_mandir}/man1/pcre2grep.1*
%{_mandir}/man1/pcre2test.1*

%files devel
%{_bindir}/pcre2-config
%{_mandir}/man1/pcre2-config.1*
%{_includedir}/pcre2.h
%{_includedir}/pcre2posix.h
%{_libdir}/libpcre2-8.so
%{_libdir}/libpcre2-16.so
%{_libdir}/libpcre2-32.so
%{_libdir}/libpcre2-posix.so
%{_libdir}/pkgconfig/libpcre2-8.pc
%{_libdir}/pkgconfig/libpcre2-16.pc
%{_libdir}/pkgconfig/libpcre2-32.pc
%{_libdir}/pkgconfig/libpcre2-posix.pc
%{_mandir}/man3/pcre2*.3*
