%global source0_hash d07563f5e787909d16e7390241e877f49ab739b1de9d0e2ea1a41bd0bf4474bc

Name:           perl-Proc-WaitStat
Version:        1.00
Release:        45%{?dist}
Summary:        Interpret and act on wait() status values

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-WaitStat
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROSCH/Proc-WaitStat-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime dependencies
BuildRequires:  perl(IPC::Signal)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IPC::Signal)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
This module contains functions for interpreting and acting on wait
status values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-WaitStat-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc README Changes
%{perl_vendorlib}/Proc*
%{_mandir}/man3/Proc*.3*

%changelog
%autochangelog
