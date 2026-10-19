%global source0_hash 54c9376b2553cb93a7958c6c8ab4c4ec9a4691b7e188acd34e80442c6a1d37d3
Name:           perl-MooX-HasEnv
Version:        0.004
Release:        33%{?dist}
Summary:        Making attributes based on ENV variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-HasEnv
Source0:        https://cpan.metacpan.org/modules/by-module/MooX/MooX-HasEnv-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moo) >= 0.009014
Requires:       perl(Package::Stash) >= 0.33
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Package::Stash\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Test::LoadAllModules)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package allows the making of attributes based on ENV variables.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-HasEnv-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

RELEASE_TESTING=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
