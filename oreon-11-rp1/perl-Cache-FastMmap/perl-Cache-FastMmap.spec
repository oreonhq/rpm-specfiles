%global source0_hash 9b2d3b0aef095d2c59b356a4482950d0c3a22e84e6e69b97bb96dcc1edc642ff

Name:           perl-Cache-FastMmap
Version:        1.60
Release:        2%{?dist}
Summary:        Uses an mmap'ed file to act as a shared memory interprocess cache
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/Cache::FastMmap
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBM/Cache-FastMmap-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Optional run-time
BuildRequires:  perl(Compress::Zlib)
# Tests
BuildRequires:  perl(Data::Dumper)
# ExtUtils::testlib not used
# lib not used
# POSIX not used
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
# Optional tests
# Do not BR GTop to disable test t/6.t because it fails randomly against
# Perl 5.24 on x86_64 arch (CPAN RT#39342)
# BuildRequires:  perl(GTop)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Sereal)

%description
In multi-process environments (eg mod_perl, forking daemons, etc),
it's common to want to cache information, but have that cache shared
between processes. Many solutions already exist, and may suit your
situation better.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-FastMmap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorarch}/auto/Cache*
%{perl_vendorarch}/Cache*
%{_mandir}/man3/Cache::FastMmap*

%changelog
%autochangelog
