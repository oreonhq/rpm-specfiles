%global source0_hash b36f3fae91590cb20a6c54f80c6be6b2b2d6ca92247a2a30aab73d88647002ff

Name:           perl-JSON-Path
Version:        1.0.6
Release:        5%{?dist}
Summary:        Search nested hashref/arrayref structures using JSONPath

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON-Path
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POPEFELIX/JSON-Path-%{version}.tar.gz

BuildArch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.16.0
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LV)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test2::V0)

# Those are only needed when building for RHEL, on Fedora they come in as
# dependencies of the above
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  perl(CPAN)
%endif

%description
This module implements JSONPath, an XPath-like language for searching JSON-
like structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Path-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
%autochangelog
