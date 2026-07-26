%global source0_hash dbd3e435b88b3c25b85f9de9455fc5a98533d3a4a44b204170b800db4e456b2b

Name:           perl-GTop
Version:        0.18
Release:        48%{?dist}
Summary:        Perl interface to libgtop
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GTop
Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJH/GTop-%{version}.tar.gz

# core
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
# non-perl
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgtop2-devel
BuildRequires:  make

%?perl_default_filter

%description
This is a perl interface to the libgtop library, useful for collecting
real-time performance and other system statistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GTop-%{version}

# rpmlint pacifications...
find . -type f -exec chmod -c -x {} \;
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' examples/*

# thread funkiness on ppc/s390
%ifarch ppc ppc64 s390
mv t/threads.t t/threads.t.disable
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO examples/ t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/GTop*
%exclude %{perl_vendorarch}/config.pl
%{_mandir}/man3/*

%changelog
%autochangelog
