# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 08d268384365dec42a8e9e2dd2c39b87f8afe2d5bacc48e2e93ad8379169e4bd
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Tests require accessible syslog
%bcond_with test

Name:           perl-Unix-Syslog
Version:        1.1
Release:        55%{?dist}
Summary:        Perl interface to the UNIX syslog(3) calls
License:        Artistic-2.0
URL:            https://metacpan.org/release/Unix-Syslog
Source0:        https://cpan.metacpan.org/authors/id/M/MH/MHARNISCH/Unix-Syslog-1.1.tar.gz

# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
%if %{with test}
BuildRequires:  syslog
%endif
# Dependencies
Requires:       syslog

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides an interface to the system logger syslogd(8) via
Perl's XSUBs. The implementation attempts to resemble the native
libc-functions of your system, so that anyone being familiar with
syslog.h should be able to use this module right away.

%prep
%oreon_verify_sources
%setup -q -n Unix-Syslog-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%if %{with test}
make test
%endif

%files
%license Artistic
%doc README Changes
%{perl_vendorarch}/Unix/
%{perl_vendorarch}/auto/Unix/
%{_mandir}/man3/Unix::Syslog.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-55
- Prepare for Oreon 11 (RP1)
