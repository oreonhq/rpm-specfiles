# Run optional test
%if ! (0%{?rhel})
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
# rm -rf doc
# Source0:      https://cpan.metacpan.org/modules/by-module/Class/Class-Data-Inheritable-%%{version}.tar.gz
Source0:        Class-Data-Inheritable-%{version}-clean.tar.gz
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
%setup -q -n Class-Data-Inheritable-%{version}

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10-4
- Prepare for Oreon 11 (RP1)
