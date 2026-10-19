%global source0_hash 2b887c1264565bff92fe7cae5046b987fe0f8cb1dd317b9e0ba18e5f2240a06a
Name:       perl-AppConfig-Std
Version:    1.10
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:        Provides standard configuration options
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-Std-%{version}.tar.gz
Url:        https://metacpan.org/release/AppConfig-Std
BuildArch:  noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AppConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl-generators
# /oreon:deps
%description
AppConfig::Std is a Perl module that provides a set of standard
configuration variables and command-line switches. It is implemented as a
subclass of AppConfig; AppConfig provides a general mechanism for handling
global configuration variables.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AppConfig-Std-%{version}

perl -pi -e 's|^#!\./perl|#!/usr/bin/perl|' t/*

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
