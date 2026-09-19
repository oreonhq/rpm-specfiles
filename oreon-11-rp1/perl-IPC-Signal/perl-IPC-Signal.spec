%global source0_hash 7c21f9c8c2d0c0f0f0f46e77de7c3d879dd562668ddf0525875c38cef2076fd0

Name:           perl-IPC-Signal
Version:        1.00
Release:        45%{?dist}
Summary:        Utility functions dealing with signals for Perl 
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/IPC-Signal
Source0:        https://cpan.metacpan.org/modules/by-module/IPC/IPC-Signal-%{version}.tar.gz

BuildArch:      noarch 
# build dependencies
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime dependencies
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
This Perl module contains utility functions for dealing with signals. 
Currently these are just translating between signal names and signal 
numbers and vice versa. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-Signal-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/IPC
%{_mandir}/man3/IPC::Signal.3pm*

%changelog
%autochangelog
