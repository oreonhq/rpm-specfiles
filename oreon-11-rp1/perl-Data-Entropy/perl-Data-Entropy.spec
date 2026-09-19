%global source0_hash 18a52b1386e82c6b8cdb384a39861d60220a442a790e077010be72dd853b67b3

Name:           perl-Data-Entropy
Version:        0.008
Release:        4%{?dist}
Summary:        Entropy (randomness) management
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-Entropy
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Data-Entropy-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom) >= 0.36
BuildRequires:  perl(Data::Float) >= 0.008
BuildRequires:  perl(Errno) >= 1.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Lite) >= 2.2
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(Math::BigInt) >= 1.16
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Crypt::Rijndael)
Requires:       perl(Crypt::URandom) >= 0.36

%{?perl_default_filter}

%description
This module maintains a concept of a current selection of entropy source.
Algorithms that require entropy, such as those in
Data::Entropy::Algorithms, can use the source nominated by this module,
avoiding the need for entropy source objects to be explicitly passed
around. This is convenient because usually one entropy source will be used
for an entire program run and so an explicit entropy source parameter would
rarely vary. There is also a default entropy source, avoiding the need to
explicitly configure a source at all.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Entropy-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
