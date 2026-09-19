%global source0_hash eb38aa93f93e8ab282d97e2582fbaea88b3f889a08cbc9dbf20059c3779d5cd8

Name:           liboping
Version:        1.10.0
Release:        36%{?dist}
Summary:        A C library to generate ICMP echo requests

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://noping.cc/
Source0:        https://noping.cc/files/%{name}-%{version}.tar.bz2
# Disable -Werror to avoid https://github.com/octo/liboping/issues/38
Patch0:         liboping-1.10.0-no-werror.patch
# Fix build with ncurses-6.3 https://github.com/octo/liboping/pull/61
# Note: slightly tweaked, since we don't have
#       https://github.com/octo/liboping/commit/47130cb9c2cdc900acf1daca1d028c87eccd2004
Patch1:         liboping-1.10.0-ncurses-6.3.patch

BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  ncurses-devel
BuildRequires:  make

%description
Liboping is a C library to generate ICMP echo requests, better known as
"ping packets". It is intended for use in network monitoring applications
or applications that would otherwise need to fork ping(1) frequently.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains files needed to develop and build software against
liboping, a %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
# The application uses a local copy of libtool, we need to remove rpath with the
# following two lines (see https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make -C src %{?_smp_mflags}
make -C bindings %{?_smp_mflags} perl/Makefile
cd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor TOP_BUILDDIR=..
%make_build

%install
make -C src install DESTDIR=%{buildroot}
cd bindings/perl
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
LD_LIBRARY_PATH=../../src/.libs make -C bindings/perl test

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/oping
%{_bindir}/noping
%{_libdir}/liboping.so.*
%{_mandir}/man8/oping.8*
%{_mandir}/man3/Net::Oping.3pm*
%{perl_vendorarch}/*
%exclude %{_libdir}/liboping.la

%files devel
%{_includedir}/oping.h
%{_libdir}/liboping.so
%{_libdir}/pkgconfig/liboping.pc
%{_mandir}/man3/liboping.3*
%{_mandir}/man3/ping_construct.3*
%{_mandir}/man3/ping_get_error.3*
%{_mandir}/man3/ping_host_add.3*
%{_mandir}/man3/ping_iterator_get.3*
%{_mandir}/man3/ping_iterator_get_context.3*
%{_mandir}/man3/ping_iterator_get_info.3*
%{_mandir}/man3/ping_send.3*
%{_mandir}/man3/ping_setopt.3*

%changelog
%autochangelog
