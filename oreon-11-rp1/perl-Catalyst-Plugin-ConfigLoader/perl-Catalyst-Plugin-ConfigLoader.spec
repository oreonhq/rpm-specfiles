%global source0_hash 9e2a698a6f2d046e0dc5e57512929cd423c807d4a36ba3f29e9e5adcd71a1971

Name:           perl-Catalyst-Plugin-ConfigLoader
Summary:        Load config files of various types
Version:        0.35
Release:        17%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-ConfigLoader-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-ConfigLoader
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime) >= 5.7008
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Config::Any) >= 0.20
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Visitor) >= 0.24
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(MRO::Compat) >= 0.09
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
BuildRequires:  sed

Requires:       perl(Catalyst::Runtime) >= 5.7008
Requires:       perl(Config::Any) >= 0.20
Requires:       perl(Data::Visitor) >= 0.24
Requires:       perl(MRO::Compat) >= 0.09

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module will attempt to load find and load a configuration file of
various types. Currently it supports YAML, JSON, XML, INI and Perl formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-ConfigLoader-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
