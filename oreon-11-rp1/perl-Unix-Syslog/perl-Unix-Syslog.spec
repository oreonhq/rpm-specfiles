%global source0_hash 08d268384365dec42a8e9e2dd2c39b87f8afe2d5bacc48e2e93ad8379169e4bd
%bcond_with test
Name:           perl-Unix-Syslog
Version:        1.1
Release:        55%{?dist}
Summary:        Perl interface to the UNIX syslog(3) calls
License:        Artistic-2.0
URL:            https://metacpan.org/release/Unix-Syslog
Source0:        https://cpan.metacpan.org/modules/by-module/Unix/Unix-Syslog-%{version}.tar.gz
%if %{with test}
%endif
Requires:       syslog
%{?perl_default_filter}
Provides:       perl(Unix::Syslog)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  syslog
# /oreon:deps
%description
This module provides an interface to the system logger syslogd(8) via
Perl's XSUBs. The implementation attempts to resemble the native
libc-functions of your system, so that anyone being familiar with
syslog.h should be able to use this module right away.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unix-Syslog-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%if %{with test}
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-55
- Prepare for Oreon 11 (RP1)
