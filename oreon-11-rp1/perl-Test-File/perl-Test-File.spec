%global source0_hash 8f1cc36b871493dfdac29bda459763711b5fd828895c0f326b6c8654babd5f09

# This module usually ships with version numbers having two digits after the decimal point
%global cpan_version 1.995
%global rpm_version 1.99.5

Summary:	Test file attributes through Test::Builder
Name:		perl-Test-File
Version:	%{rpm_version}
Release:	3%{?dist}
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-File
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-File-%{cpan_version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(ExtUtils::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::Builder) >= 1.001006
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More) >= 1
BuildRequires:	perl(utf8)
BuildRequires:	perl(version) >= 0.86
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
# (none)

Provides:       perl(Test::File)
%description
This module provides a collection of test utilities for file attributes.

Some file attributes depend on the owner of the process testing the file
in the same way the file test operators do.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-File-%{cpan_version}

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
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::File.3*

%changelog
%autochangelog
