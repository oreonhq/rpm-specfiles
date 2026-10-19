%global source0_hash 437eebed042093b365c1a90c65e53bf9ca2859dd889a0ae845fe9f9da3c6c006
Name:           perl-Algorithm-Loops
Version:        1.032
Release:        24%{?dist}
Summary:        Perl module for looping constructs
License:        Unlicense
URL:            https://metacpan.org/release/Algorithm-Loops
Source0:        https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Loops-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Algorithm::Loops provides several functions (NestedLoops, MapCar*, Filter, 
and NextPermute*) for doing different types of looping constructs. By 
default, no functions are exported into a namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Algorithm-Loops-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
