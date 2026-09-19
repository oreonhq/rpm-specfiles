%global source0_hash c5ff5db2ce6139452bd30b18cd1662d05cdce7931c939e3a9930bfaf91cfe5b3

Summary:	Pull out the modules a module explicitly uses
Name:		perl-Module-Extract-Use
Version:	1.054
Release:	3%{?dist}
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-Use
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-Use-%{version}.tar.gz
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
BuildRequires:	perl(Test::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(PPI)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(Test::More) >= 1.0
BuildRequires:	perl(version) >= 0.86
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(PPI)

%description
Extract the names of the modules used in a file using a static analysis. Since
this module does not run code, it cannot find dynamic uses of modules, such as
eval "require $class". It only reports modules that the file loads directly.
Modules loaded with parent or base, for instance, will be in the import list
for those pragmas but won't have separate entries in the data this module
returns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Extract-Use-%{version}

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
%doc Changes examples/ README.pod SECURITY.md
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Extract::Use.3*

%changelog
%autochangelog
