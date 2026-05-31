%global source0_hash 2097ca273f8947bd62b1c19d40e1111eb106011338ae6be9f2f37cc88911d006

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Package_Generator_enables_extra_test
%else
%bcond_with perl_Package_Generator_enables_extra_test
%endif

Name:		perl-Package-Generator
Version:	1.106
Release:	35%{?dist}
Summary:	Generate new packages quickly and easily
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Generator
Source0:        https://cpan.metacpan.org/modules/by-module/Package/Package-Generator-%{version}.tar.gz



BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Params::Util) >= 0.11
BuildRequires:	perl(Test::More) >= 0.96
%if %{with perl_Package_Generator_enables_extra_test}
# Extra Tests
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
# Runtime

%description
This module lets you quickly and easily construct new packages. It gives
them unused names and sets up their package data, if provided.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Package-Generator-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_Package_Generator_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Package/
%{_mandir}/man3/Package::Generator.3*
%{_mandir}/man3/Package::Reaper.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.106-35
- Prepare for Oreon 11 (RP1)
