%global source0_hash 777d64d2938f5ea586300eef97ef03eacb43d4c1853c9c3b1091eb3311467970
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%ifarch %{ix86} x86_64 ppc s390x %{arm} aarch64 ppc64 ppc64le
%global with_valgrind 1
%endif
Name:		perl-Test-LeakTrace
Summary:        Trace memory leaks
Version:	0.17
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-LeakTrace
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-LeakTrace-%{version}.tar.gz
%if !%{defined perl_bootstrap}
%if 0%{?with_valgrind}
%endif
%endif
%{?perl_default_filter}
Provides:       perl(Test::LeakTrace)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Spellunker)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(autouse)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Test::LeakTrace provides several functions that trace memory leaks. This module
scans arenas, the memory allocation system, so it can detect any leaked SVs in
given blocks.

Leaked SVs are SVs that are not released after the end of the scope they have
been created. These SVs include global variables and internal caches. For
example, if you call a method in a tracing block, perl might prepare a cache
for the method. Thus, to trace true leaks, no_leaks_ok() and leaks_cmp_ok()
executes a block more than once.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-LeakTrace-%{version}

# Remove redundant exec bits
chmod -c -x lib/Test/LeakTrace/Script.pm t/lib/foo.pl

# Fix up shellbangs in doc scripts
sed -i -e 's|^#!perl|#!/usr/bin/perl|' benchmark/*.pl example/*.{pl,t} {t,xt}/*.t

# Don't try to run the valgrind test whilst bootstrapping
%if %{defined perl_bootstrap} || ! 0%{?with_valgrind}
rm xt/05_valgrind.t
sed -i -e '/^xt\/05_valgrind\.t/d' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
