%global source0_hash 6228bd38e884550a076f8303c32c07dc53f04d0a334dd0e65e1d80ef5102c604
Name:           perl-Sub-Exporter-Lexical
Version:        1.001
Release:        1%{?dist}
Summary:        Export lexically-available subs with Sub::Exporter
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Exporter-Lexical
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-Lexical-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Sub::Exporter::Lexical)
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lexical::Sub)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Sub::Exporter::Lexical provides an alternate installer for Sub::Exporter.
Installers are documented in Sub::Exporter's documentation; all you need to
know is that by using Sub::Exporter::Lexical's installer, you can import
routines into a lexical scope that will be cleaned up when that scope ends.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Exporter-Lexical-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
rm $RPM_BUILD_ROOT%{perl_vendorlib}/Sub/Exporter/snippet.pl
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
