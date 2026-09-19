%global source0_hash 2d5d12b343f57de90029ee13c66f7fe0494b3af54b286f00e327ec2a1f976e68

Name:           perl-Hash-Layout
Version:        2.00
Release:        16%{?dist}
Summary:        Hashes with predefined levels, composite keys and default values
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Hash-Layout
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANSTYN/Hash-Layout-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Clone)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Hash::Layout provides deep hashes with a predefined number of levels which
you can access using special "composite keys". These are essentially string
paths that inflate into actual hash keys according to the defined levels
and delimiter mappings, which can be the same or different for each level.
This is useful both for shorter keys as well as merge/fallback to default
values, such as when defining overlapping configs ranging from broad to
narrowing scope.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-Layout-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README README.md
%license LICENSE
%{perl_vendorlib}/Hash*
%{_mandir}/man3/Hash*

%changelog
%autochangelog
