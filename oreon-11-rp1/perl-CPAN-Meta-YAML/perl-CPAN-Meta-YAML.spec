%global source0_hash 36c45e0e954fb6d9e4b71ce3da4a244157439969a3af12c515909d7d6c053b2c

# Run extra test
%if 0%{!?perl_bootstrap:1}
%if ! (0%{?rhel})
%bcond_without perl_CPAN_Meta_YAML_enables_extra_test
%else
%bcond_with perl_CPAN_Meta_YAML_enables_extra_test
%endif
%else
# Don't run extra tests when bootstrapping as many of those
# tests' dependencies build-require this package
%global _without_perl_CPAN_Meta_YAML_enables_extra_test 1
%global _with_perl_CPAN_Meta_YAML_enables_extra_test 0
%endif

Name:		perl-CPAN-Meta-YAML
Version:	0.020
Release:	522%{?dist}
Summary:	Read and write a subset of YAML for CPAN Meta files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Meta-YAML
Source0:        https://www.cpan.org/modules/by-module/CPAN/CPAN-Meta-YAML-%{version}.tar.gz

BuildArch:	noarch
# Build:
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime:
BuildRequires:	perl(B)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Tests:
BuildRequires:	perl(base)
# CPAN::Meta requires CPAN::Meta::YAML
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
%endif
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(lib)
BuildRequires:	perl(open)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(utf8)
BuildRequires:	perl(vars)
%if %{with perl_CPAN_Meta_YAML_enables_extra_test}
# Extra Tests:
BuildRequires:	perl(blib)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Version)
%endif
# Dependencies
Requires:	perl(Carp)
Requires:	perl(Fcntl)

%description
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n CPAN-Meta-YAML-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 UNINST=0
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_CPAN_Meta_YAML_enables_extra_test}
make test TEST_FILES="xt/*/*.t"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::YAML.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.020-522
- Prepare for Oreon 11 (RP1)
