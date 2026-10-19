%global source0_hash 4bd7217e636601a1b17a79c9dfbd3656c6db8bc8baa66f0d376c7a321dc0dc17
Name:		perl-Module-Extract-Namespaces
Version:	1.026
Release:        3%{?dist}
Summary:        Extract the package declarations from a module
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-Namespaces
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-Namespaces-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Test::Manifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module extracts package declarations from Perl code without running the
code.

It does not extract:

 * Packages declared dynamically (e.g. in eval)
 * Packages created as part of a fully qualified variable name

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Extract-Namespaces-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
