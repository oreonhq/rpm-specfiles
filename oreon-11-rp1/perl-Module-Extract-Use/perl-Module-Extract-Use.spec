%global source0_hash c5ff5db2ce6139452bd30b18cd1662d05cdce7931c939e3a9930bfaf91cfe5b3
Summary:        Pull out the modules a module explicitly uses
Name:		perl-Module-Extract-Use
Version:	1.054
Release:        1%{?dist}
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-Use
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-Use-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(PPI)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
