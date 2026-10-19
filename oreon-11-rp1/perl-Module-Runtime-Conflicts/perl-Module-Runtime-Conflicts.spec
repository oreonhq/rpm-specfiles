%global source0_hash 707cdc75038c70fe91779b888ac050f128565d3967ba96680e1b1c7cc9733875
Name:           perl-Module-Runtime-Conflicts
Version:        0.003
Release:        1%{?dist}
Summary:        Provide information on conflicts for Module::Runtime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Runtime-Conflicts
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Runtime-Conflicts-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::CheckConflicts)
%{?perl_default_filter}
Provides:       perl(Module::Runtime::Conflicts)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Dist::CheckConflicts)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides conflicts checking for Module::Runtime, which had a
recent release that broke some versions of Moose. It is called from
Moose::Conflicts and moose-outdated.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Runtime-Conflicts-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
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
