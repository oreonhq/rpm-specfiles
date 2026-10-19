%global source0_hash be1b6f5a3eef125a44e5daf2bfdf05d4f1b4161badc7dc82bcc84b8c8231535e
Name:           perl-Gearman-Server
Version:        1.130.1
Release:        1%{?dist}
Summary:        Function call router and load balancer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gearman-Server
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALIK/Gearman-Server-v%{version}.tar.gz
Patch0:         Gearman-Server-v1.130.0-Do-not-use-usr-bin-env.patch
Patch1:         Gearman-Server-v1.130.1-Load-IO-Socket-INET.patch
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Danga::Socket\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Danga::Socket)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gearman::Util)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
