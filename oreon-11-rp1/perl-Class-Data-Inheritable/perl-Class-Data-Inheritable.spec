%global source0_hash aa1ae68a611357b7bfd9a2f64907cc196ddd6d047cae64ef9d0ad099d98ae54a

# Run optional test
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Class_Data_Inheritable_enables_optional_test
%else
%bcond_with perl_Class_Data_Inheritable_enables_optional_test
%endif

Name:           perl-Class-Data-Inheritable
Version:        0.10
Release:        4%{?dist}
Summary:        Inheritable, overridable class data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Data-Inheritable
# has non-free and possibly outdated jp docs
# Source0:      https://cpan.metacpan.org/modules/by-module/Class/Class-Data-Inheritable-%%{version}.tar.gz
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSHERER/Class-Data-Inheritable-0.10.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)
%if %{with perl_Class_Data_Inheritable_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
Requires:       perl(Carp)

%description
Class::Data::Inheritable is for creating accessor/mutators to 
class data. That is, if you want to store something about your 
class as a whole (instead of about a single object). This data 
is then inherited by your sub-classes and can be overridden.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Data-Inheritable-%{version}
rm -rf doc

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Data::Inheritable.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10-4
- Import
