%global source0_hash fbda92d37e0481d18eebc81e48d025228b57184c59b2d5a6f6bdf87042e8c7b2
Name:           perl-Test-Exit
Version:        0.11
Release:        25%{?dist}
Summary:        Test that some code calls exit without terminating testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Exit
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Test-Exit-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::Builder::Module) >= 0.86
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Builder::Module\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Return::MultiLevel)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Exit Perl module provides some simple tools for testing code that might
call exit(), providing you with the status code without exiting the test file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Exit-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
