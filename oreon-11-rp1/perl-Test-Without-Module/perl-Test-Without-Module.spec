%global source0_hash 8289e1cd7f57017a816ab4127e29ecd7a754ae7cd5c037c41b3b3bf849c21d21
Name:           perl-Test-Without-Module
Version:        0.23
Release:        1%{?dist}
Summary:        Test fallback behavior in absence of modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Without-Module
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Without-Module-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
Provides:       perl(Test::Without::Module)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows you to deliberately hide modules from a program even
though they are installed. This is mostly useful for testing modules that
have a fallback when a certain dependency module is not installed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Without-Module-%{version}
perl -pi -e 's/\r//' README Changes
chmod 644 README Changes

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23-4
- Prepare for Oreon 11 (RP1)
