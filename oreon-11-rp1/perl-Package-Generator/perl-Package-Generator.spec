%global source0_hash 2097ca273f8947bd62b1c19d40e1111eb106011338ae6be9f2f37cc88911d006
%bcond_with perl_Package_Generator_enables_extra_test
Name:		perl-Package-Generator
Version:	1.106
Release:        35%{?dist}
Summary:        Generate new packages quickly and easily
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Package-Generator
Source0:        https://cpan.metacpan.org/modules/by-module/Package/Package-Generator-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Package_Generator_enables_extra_test}
%endif
Provides:       perl(Package::Generator)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%if %{with perl_Package_Generator_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.106-35
- Prepare for Oreon 11 (RP1)
