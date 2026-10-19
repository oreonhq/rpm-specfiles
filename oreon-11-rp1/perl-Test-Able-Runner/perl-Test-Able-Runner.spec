%global source0_hash 1af0579e28a2c6a83203be3bf234a4d968fb901471cc63b82c935653e81052c9
Name:           perl-Test-Able-Runner
Version:        1.002
Release:        1%{?dist}
Summary:        Use Test::Able without a bunch of boilerplate
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Able-Runner
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HANENKAMP/Test-Able-Runner-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Load) >= 0.20
Requires:       perl(Module::Pluggable) >= 3.6
Requires:       perl(Moose) >= 0.94
Requires:       perl(Test::Able) >= 0.09
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Module::Pluggable|Moose|Test::Able|Class::Load)\\)\\s*$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Able)
BuildRequires:  perl(Test::Able::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
I like Test::Able. I really don't like having to copy my boilerplate test
runner and modify it when I use it in a new project. This provides a basic
test runner for your testable tests that takes care of the basics for you.
You can extend it a bit to customize things if you like as well. Let me
know if you want this to do something else.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Able-Runner-%{version}
# Remove stray files, CPAN RT#92579
rm lib/Test/Able/Runner/Role/Meta/Class.pm.{orig,rej}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
