%global source0_hash 172b345e3b65b19697a0ac513fe6ac1f20ef8fe5ed3d88cd425c2b4febc45df5

Name:		perl-Module-Extract-VERSION
Version:	1.119
Release:	3%{?dist}
Summary:	Extract a module version without running code
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-VERSION
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-VERSION-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Safe)
BuildRequires:	perl(strict)
BuildRequires:	perl(version) >= 0.86
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More) >= 1
# Optional Tests
BuildRequires:	perl(Test::Manifest) >= 1.21
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(Safe)
Requires:	perl(version) >= 0.86

%description
This module lets you pull out of module source code the version number for the
module. It assumes that there is only one $VERSION in the file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Extract-VERSION-%{version}

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
%{_mandir}/man3/Module::Extract::VERSION.3*

%changelog
%autochangelog
