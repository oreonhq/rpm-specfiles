%global source0_hash 9ecb8258ef30c2f24deff4917240d0fe73242da5b2192402f79815b092ed36e3

Name:           perl-Log-Trace
Version:        1.070
Release:        48%{?dist}
License:        GPL-2.0-or-later
Summary:        A unified approach to tracing
Source:         https://cpan.metacpan.org/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
Url:            https://metacpan.org/release/Log-Trace
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Serializer)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Recommends:     perl(Data::Dumper)
Recommends:     perl(Data::Serializer)
Recommends:     perl(Sys::Syslog)
Recommends:     perl(Time::HiRes)

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)$

Provides:       perl(Log::Trace)
%description
This module provides a unified approach to tracing. A script can 'use
Log::Trace qw( < mode > )' to set the behaviour of the TRACE function.By
default, the trace functions are exported to the calling package only.
You can export the trace functions to other packages with the 'Deep'
option. See the "OPTIONS" manpage for more information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Log-Trace-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc README Changes
%{perl_vendorlib}/Log*
%{_mandir}/man3/Log::Trace*.3*

%changelog
%autochangelog
