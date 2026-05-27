%global source0_hash 81462da3cd9e745901f29ff006c4c804cc9db017ccf45154b3cd9558540bc191

# Run extra tests
%if 0%{?fedora} || 0%{?rhel} > 6
%bcond_without perl_Software_License_enables_extra_test
%else
%bcond_with perl_Software_License_enables_extra_test
%endif
# Run optional tests
%if 0%{!?perl_bootstrap:1} && 0%{?fedora}
%bcond_without perl_Software_License_enables_optional_test
%else
%bcond_with perl_Software_License_enables_optional_test
%endif

Name:           perl-Software-License
Version:        0.104007
Release:        3%{?dist}
Summary:        Package that provides templated software licenses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Software-License
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
%if %{with perl_Software_License_enables_optional_test}
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Software::License::CCpack)
%endif
%if %{with perl_Software_License_enables_extra_test}
# Extra Tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::Pod)
%endif
# Dependencies
# (none)

%description
Software-License contains templates for common open source software licenses.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Software-License-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%{make_build} test
%if %{with perl_Software_License_enables_extra_test}
%{make_build} test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Software/
%{_mandir}/man3/Software::License.3*
%{_mandir}/man3/Software::License::*.3*
%{_mandir}/man3/Software::LicenseUtils.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.104007-3
- Prepare for Oreon 11 (RP1)
