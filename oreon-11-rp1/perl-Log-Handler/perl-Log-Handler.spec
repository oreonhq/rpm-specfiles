%global source0_hash 3a5c80e7128454770f83acab8cbd3e70e5ec3d59a61dc32792a178f0b31bf74d

%global pkgname Log-Handler

Name:           perl-Log-Handler
Version:        0.90
Release:        16%{?dist}
Summary:        Log messages to several outputs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Url:            https://metacpan.org/release/Log-Handler
Source0:        https://cpan.metacpan.org/modules/by-module/Log/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Config::Properties)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Email::Date)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
# IO::Socket::INET
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(warnings)
# YAML
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildArch:      noarch

%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_docdir}/

%description
This module is a object oriented handler for logging, tracing and debugging. 
It is very easy to use and provides a simple interface for multiple output 
objects with lots of configuration parameters. You can easily filter the 
amount of logged information on a per-output base, define priorities, create 
patterns to format the messages and reload the complete logging machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version} 

%build
perl Makefile.PL NO_PERLLOCAL=1 NO_PACKLIST=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc ChangeLog README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
