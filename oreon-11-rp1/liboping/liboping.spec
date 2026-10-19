%global source0_hash eb38aa93f93e8ab282d97e2582fbaea88b3f889a08cbc9dbf20059c3779d5cd8
Name:           liboping
Version:        1.10.0
Release:        36%{?dist}
Summary:        A C library to generate ICMP echo requests
License:        GPL-2.0-only
URL:            https://noping.cc/
Source0:        https://noping.cc/files/%{name}-%{version}.tar.bz2
Patch0:         liboping-1.10.0-no-werror.patch
Patch1:         liboping-1.10.0-ncurses-6.3.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_prep
%build

%configure --disable-static
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=../../src/.libs make -C bindings/perl test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n liboping-devel -f %{oreon_filedir}/liboping-devel.list

%changelog

%autochangelog
