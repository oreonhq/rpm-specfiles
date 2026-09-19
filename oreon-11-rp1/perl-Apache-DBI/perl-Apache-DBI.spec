%global source0_hash 9d7d520da7e579756a032021bcdbe61a3a3e5fae90df767f0cea08b3c666e677

Name:      perl-Apache-DBI
Version:   1.12
Release:   37%{?dist}
Summary:   Persistent database connections with Apache/mod_perl

License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/Apache-DBI
Source0:   https://cpan.metacpan.org/authors/id/P/PH/PHRED/Apache-DBI-%{version}.tar.gz

BuildArch: noarch
# build deps
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# runtime deps
# perl(Apache) never used because we deliver mod_perl >= 2
# perl(Apache2::Access) not used at tests
# perl(Apache2::Const) not used at tests
# perl(Apache2::Log) not used at tests
# perl(Apache2::Module) not used at tests
# perl(Apache2::RequestRec) not used at tests
# perl(Apache2::RequestUtil) not used at tests
# perl(Apache2::ServerUtil) not used at tests
# perl(Apache::Constants) never used because we deliver mod_perl >= 2
BuildRequires: perl(Carp)
BuildRequires: perl(DBI) >= 1.00
# perl(Digest::MD5) >= 2.20 not used at tests
# perl(Digest::SHA1) >= 2.01 not used at tests
# perl(IPC::SysV) not used at tests
# perl(ModPerl::Util) not used at tests
BuildRequires: perl(constant)
# perl(mod_perl2) not used at tests
BuildRequires: perl(strict)
# perl(warnings) not used at tests
# test deps
BuildRequires: perl(DBD::mysql)
BuildRequires: perl(Test::More)
# Apache::DBI can be used as a compatibility layer in CGI scripts out of
# mod_perl environment. Then Apache2 modules are not loaded. Keep them
# optional.
# perl(Apache) is never used. We deliver mod_perl >= 2.
Recommends: perl(Apache2::Module)
Recommends: perl(Apache2::RequestUtil)
Recommends: perl(Apache2::ServerUtil)
Requires:   perl(DBI) >= 1.00
Recommends: perl(ModPerl::Util)
Recommends: perl(mod_perl2)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DBI|Digest::MD5|Digest::SHA1)\\)$

%description
This is version %{version} of Apache::DBI.

This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provises support for
persistent database connections via Perl's Database Independent Interface
(DBI):

  - connections can be established during server-startup 
  - configurable rollback to ensure data integrity 
  - configurable verification of the connections to avoid time-outs. 

Apache::DBI has been in widespread deployment on many platforms for
years.  Apache::DBI is one of the most widely used mod_perl related
modules.  It can be considered stable.

%package -n perl-Apache-AuthDBI
Summary:   Authentication and Authorization via Perl's DBI
# Split from perl-Apache-DBI in Fedora 40
Conflicts: perl-Apache-DBI < 1.12-31
Requires:   perl(Apache2::Access)
Requires:   perl(Apache2::Const)
Requires:   perl(Apache2::Log)
Requires:   perl(Apache2::RequestRec)
# Apache::AuthDBI requires mod_perl. We deliver mod_perl >= 2. Therefore hard
# require modules used with mod_perl >= 2 and do not requiree mod_perl 1
# modules.
Requires:   perl(Apache2::RequestUtil)
Requires:   perl(Apache2::ServerUtil)
Requires:   perl(DBI) >= 1.00
Requires:   perl(Digest::MD5) >= 2.20
Requires:   perl(Digest::SHA1) >= 2.01
Requires:   perl(IPC::SysV)
Requires:   perl(warnings)

%description -n perl-Apache-AuthDBI
This is version %{version} of Apache::AuthDBI.

This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provides support for basic
authentication and authorization via Perl's Database Independent Interface
(DBI):

  - optional shared cache for passwords to minimize database load
  - configurable cleanup-handler deletes outdated entries from the cache

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-DBI-%{version}
perl -pi -MConfig -e 's|^#!/usr/local/bin/perl\b|$Config{startperl}|' eg/startup.pl
chmod 644 eg/startup.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset MOD_PERL_API_VERSION
make test

%files
%doc Changes README TODO traces.txt eg/
%{_mandir}/man3/Apache::DBI.*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/DBI.pm

%files -n perl-Apache-AuthDBI
%doc Changes README TODO traces.txt eg/
%{_mandir}/man3/Apache::AuthDBI.*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/AuthDBI.pm

%changelog
%autochangelog
