%global source0_hash f2b723e8f08cde12b7d43dd68f49f136c222390f110ad85bc7cf05c6806070d9

Name:       perl-Directory-Scratch-Structured 
Version:    0.04
Release:    48%{?dist}
# see lib/Directory/Scratch/Structured.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Creates temporary files and directories from a structured description
Source:     https://cpan.metacpan.org/authors/id/N/NK/NKH/Directory-Scratch-Structured-%{version}.tar.gz 
Url:        https://metacpan.org/release/Directory-Scratch-Structured
BuildArch:  noarch

BuildRequires: make
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires: perl(Carp)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(English)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Warn)

%description
This module adds a _create_structured_tree_ subroutine to Directory::Scratch.
This method is useful to create a directory structure needed for temporary
purposes, e.g. for testing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Directory-Scratch-Structured-%{version}

find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
