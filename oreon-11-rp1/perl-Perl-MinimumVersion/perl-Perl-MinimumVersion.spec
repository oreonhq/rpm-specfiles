%global source0_hash ffa9c8a2f099660a81361eb8bac56a335793b3e160fa5b1d97078b83142ce8cb

Name:           perl-Perl-MinimumVersion
Version:        1.44
Release:        2%{?dist}
Summary:        Find a minimum required version of perl for Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-MinimumVersion
Source0:	https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Perl-MinimumVersion-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: %{__make}
BuildRequires: %{__perl}

BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
# Run-time and tests:
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::Util) >= 1.20
BuildRequires: perl(Params::Util) >= 0.25
BuildRequires: perl(Perl::Critic::Utils) >= 1.104
BuildRequires: perl(PPI) >= 1.252
BuildRequires: perl(PPI::Util)
BuildRequires: perl(PPIx::Utils)
BuildRequires: perl(PPIx::Regexp) >= 0.051
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(version) >= 0.76
BuildRequires: perl(warnings)
%if !%{defined perl_bootstrap}
BuildRequires: perl(File::Find::Rule) >= 0.32
BuildRequires: perl(File::Find::Rule::Perl) >= 1.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Script) >= 1.03
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl >= 0:5.005$

Provides:       perl(Perl::MinimumVersion)
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

%check
%if !%{defined perl_bootstrap}
%{__make} test
%endif

%files
%doc Changes
%license LICENSE
%{_bindir}/perlver*
%{perl_vendorlib}/Perl
%{_mandir}/man1/perlver*
%{_mandir}/man3/Perl::MinimumVersion*

%changelog
%autochangelog
