%global source0_hash 6260ea28bbbde6059c48efa128eac95172639201b4b4adcb5fd1f7f31423ddaa
Name:           perl-Log-Dispatch-Perl
Version:        0.05
Release:        1%{?dist}
Summary:        Use core Perl functions for logging
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Dispatch-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Log-Dispatch-Perl-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The "Log::Dispatch::Perl" module offers a logging alternative using
standard Perl core functions. It allows you to fall back to the common Perl
alternatives for logging, such as "warn" and "cluck". It also adds the
possibility for a logging action to halt the current environment, such as
with "die" and "croak".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Dispatch-Perl-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
