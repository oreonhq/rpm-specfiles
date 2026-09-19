%global source0_hash da0be319762066ef0546f54ecf42b0da6d2463a932a55e06e6161678e21078d3

Name:       perl-MooseX-Log-Log4perl
Version:    0.47
Release:    32%{?dist}
# see lib/MooseX/Log/Log4perl.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    A Logging Role for Moose based on Log::Log4perl
Source:     https://cpan.metacpan.org/authors/id/L/LA/LAMMEL/MooseX-Log-Log4perl-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Log-Log4perl
BuildArch:  noarch
Patch0:     MooseX-Log-Log4perl-0.47-Fix-building-on-Perl-without-dot-in-INC.patch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(base)
BuildRequires: perl(Config)
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(ExtUtils::MM_Unix)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FindBin)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Log::Log4perl) >= 1.13
BuildRequires: perl(Moo) >= 1.000007
BuildRequires: perl(Moo::Role)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
# optional tests
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
A logging role building a very lightweight wrapper to Log::Log4perl for use
with your the Moose classes. The initialization of the Log4perl instance must
be performed prior to logging the first log message. Otherwise the default
initialization will happen, probably not doing the things you expect.

For compatibility the 'logger' attribute can be accessed to use a common
interface for application logging.

For simple logging needs use MooseX::Log::Log4perl::Easy to directly add
log_<level> methods to your class instance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Log-Log4perl-%{version}
%patch -P0 -p1

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
TEST_AUTHOR=1 TEST_POD=1 make test

%files
%doc README Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
