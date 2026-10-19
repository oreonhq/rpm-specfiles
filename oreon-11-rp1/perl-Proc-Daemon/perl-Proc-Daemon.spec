%global source0_hash 34c0b85b7948b431cbabc97cee580835e515ccf43badbd8339eb109474089b69
%global perlname Proc-Daemon
Name:      perl-Proc-Daemon
Version:   0.23
Release:        1%{?dist}
Summary:        Run Perl program as a daemon process
License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/Proc-Daemon
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKREAL/%{perlname}-%{version}.tar.gz
BuildArch: noarch
Requires:  perl(Proc::ProcessTable)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is version %{version} of Proc::Daemon

This module contains the routine Init which can be called by a Perl 
program to initialize itself as a daemon. A daemon is a process that
runs in the background with no controlling terminal. Generally servers
(like FTP and HTTP servers) run as daemon processes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{perlname}-%{version}

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
