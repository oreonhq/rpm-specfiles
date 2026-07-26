%global source0_hash 083256255a48094fd9ac1239e0fea8a10a2383a9cd1ef4b1c7264ede1b4400ab

Name:           perl-JSON-Any
Summary:        A meta-module to make working with JSON easier
Version:        1.40
Release:        7%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-Any-%{version}.tar.gz

URL:            https://metacpan.org/release/JSON-Any
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
# Not in Fedora
# BuildRequires:  perl(JSON::DWIW)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::Syck)
BuildRequires:  perl(JSON::XS) >= 1.52
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::Without::Module)

Requires:       perl(Carp)
Requires:       perl(JSON::XS) >= 1.52

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
JSON::Any provides a coherent API to bring together the various JSON modules
currently on CPAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Any-%{version}
find .  -type f -exec chmod -c -x {} +

%build
/usr/bin/perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor --default
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
%autochangelog
