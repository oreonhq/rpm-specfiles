%global source0_hash b36f3fae91590cb20a6c54f80c6be6b2b2d6ca92247a2a30aab73d88647002ff
Name:           perl-JSON-Path
Version:        1.0.6
Release:        1%{?dist}
Summary:        Search nested hashref/arrayref structures using JSONPath
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON-Path
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POPEFELIX/JSON-Path-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LV)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
