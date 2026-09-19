%global source0_hash 4bd7217e636601a1b17a79c9dfbd3656c6db8bc8baa66f0d376c7a321dc0dc17

Name:		perl-Module-Extract-Namespaces
Version:	1.026
Release:	3%{?dist}
Summary:	Extract the package declarations from a module
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-Namespaces
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-Namespaces-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Test::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(PPI) >= 1.270
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 1
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
BuildRequires:	perl(version) >= 0.86
# Dependencies
# (none)

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

%check
make test

%files
%license LICENSE
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Extract::Namespaces.3*

%changelog
%autochangelog
