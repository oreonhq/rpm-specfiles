%global source0_hash 81462da3cd9e745901f29ff006c4c804cc9db017ccf45154b3cd9558540bc191
%bcond_with perl_Software_License_enables_extra_test
%bcond_with perl_Software_License_enables_optional_test
Name:           perl-Software-License
Version:        0.104007
Release:        1%{?dist}
Summary:        Package that provides templated software licenses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Software-License
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Software_License_enables_optional_test}
%endif
%if %{with perl_Software_License_enables_extra_test}
%endif
Provides:       perl(Software::License)
Provides:       perl(Software::LicenseUtils)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Software-License contains templates for common open source software licenses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Software-License-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%{make_build} test
%if %{with perl_Software_License_enables_extra_test}
%{make_build} test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.104007-3
- Prepare for Oreon 11 (RP1)
