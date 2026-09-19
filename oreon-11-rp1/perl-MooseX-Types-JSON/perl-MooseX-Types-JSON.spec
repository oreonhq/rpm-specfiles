%global source0_hash 3006f8bd79b0a1fc648bde0cae90a23e2cf548b3924985e450a7460c8b69c7af

Name:           perl-MooseX-Types-JSON
Summary:        JSON data types for Moose
Version:        1.01
Release:        13%{?dist}
# see lib/MooseX/Types/JSON.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/MooseX-Types-JSON-%{version}.tar.gz 
URL:            https://metacpan.org/release/MooseX-Types-JSON

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON::XS) >= 2.00
BuildRequires:  perl(JSON)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

# note the versioning here, that we don't get elsewhere
Requires:       perl(JSON::XS) >= 2.00
Requires:       perl(Moose)
Requires:       perl(MooseX::Types)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-JSON-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc README Changes examples/
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
