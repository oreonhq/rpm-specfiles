%global source0_hash ffa9c8a2f099660a81361eb8bac56a335793b3e160fa5b1d97078b83142ce8cb
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Perl-MinimumVersion
Version:        1.44
Release:        1%{?dist}
Summary:        Find a minimum required version of perl for Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-MinimumVersion
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Perl-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl >= 0:5.005$
Provides:       perl(Perl::MinimumVersion)
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Util)
BuildRequires:  perl(PPIx::Regexp)
BuildRequires:  perl(PPIx::Utils)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Find a minimum required version of perl for Perl code

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-MinimumVersion-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%if !%{defined perl_bootstrap}
%{__make} test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
