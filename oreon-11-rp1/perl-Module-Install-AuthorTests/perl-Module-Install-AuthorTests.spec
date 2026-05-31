%global source0_hash 4025722de6357edf53c28501b00e7da92cd2f9fc611ba0753761a0e1dff32d88

Name:           perl-Module-Install-AuthorTests
Version:        0.002
Release:        39%{?dist}
Summary:        Designate tests only run by module authors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-AuthorTests
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Module-Install-AuthorTests-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Build-time inc-ed:
# XXX: We cannot remove ./inc because it build-requires this module (bootstrap)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install)
# Tests:
BuildRequires:  perl(Test::More)
# Plug-in for Module::Install
Requires:       perl(Module::Install)

%description
Plug-in for Perl Module::Install package to declare tests in ./xt directory
should be run only if the module is being built by an author.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-AuthorTests-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.002-39
- Prepare for Oreon 11 (RP1)
