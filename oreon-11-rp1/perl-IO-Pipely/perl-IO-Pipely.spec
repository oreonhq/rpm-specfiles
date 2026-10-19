%global source0_hash 0e3fcd841a327efb549fa01b2083dc3695e72ea0c63303e56ed5161bf810413b
Name:           perl-IO-Pipely
Version:        0.006
Release:        11%{?dist}
Summary:        Portably create pipe() or pipe-like handles, one way or another
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Pipely
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/IO-Pipely-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(base)
Requires:       perl(Exporter) >= 5.72
Requires:       perl(Fcntl) >= 1.13
Requires:       perl(IO::Socket) >= 1.38
Requires:       perl(Symbol) >= 1.08
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(base\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Exporter\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Fcntl\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::Socket\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Symbol\\)$
Provides:       perl(IO::Pipely)
Provides:       perl(IO::Pipely)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
IO::Pipely provides a couple functions to portably create one- and two-way
pipes and pipe-like socket pairs. It acknowledges and works around known
platform issues so you don't have to.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Pipely-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
