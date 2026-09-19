%global source0_hash be1b6f5a3eef125a44e5daf2bfdf05d4f1b4161badc7dc82bcc84b8c8231535e

Name:           perl-Gearman-Server
Version:        1.130.1
Release:        29%{?dist}
Summary:        Function call router and load balancer
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gearman-Server
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALIK/Gearman-Server-v%{version}.tar.gz
# Use absolute interpreter
Patch0:         Gearman-Server-v1.130.0-Do-not-use-usr-bin-env.patch
# Load IO::Socket::INET in Gearman/Server.pm
Patch1:         Gearman-Server-v1.130.1-Load-IO-Socket-INET.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Danga::Socket) >= 1.52
BuildRequires:  perl(Errno)
BuildRequires:  perl(fields)
BuildRequires:  perl(Gearman::Util)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script) >= 1.12

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Danga::Socket\\)$

%description
You run a Gearman server (or more likely, many of them for both high-
availability and load balancing), then have workers (using Gearman::Worker
from the Gearman module, or libraries for other languages) register their
ability to do certain functions to all of them, and then clients (using
Gearman::Client, Gearman::Client::Async, etc) request work to be done from
one of the Gearman servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gearman-Server-v%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README.md
%{_bindir}/gearmand
%{perl_vendorlib}/Gearman
%{_mandir}/man1/gearmand.*
%{_mandir}/man3/Gearman::*.*

%changelog
%autochangelog
