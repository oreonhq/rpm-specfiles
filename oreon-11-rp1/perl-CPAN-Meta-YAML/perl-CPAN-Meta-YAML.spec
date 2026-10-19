%global source0_hash 36c45e0e954fb6d9e4b71ce3da4a244157439969a3af12c515909d7d6c053b2c
%if 0%{!?perl_bootstrap:1}
%bcond_with perl_CPAN_Meta_YAML_enables_extra_test
%else
%global _without_perl_CPAN_Meta_YAML_enables_extra_test 1
%global _with_perl_CPAN_Meta_YAML_enables_extra_test 0
%endif
Name:		perl-CPAN-Meta-YAML
Version:	0.020
Release:        1%{?dist}
Summary:        Read and write a subset of YAML for CPAN Meta files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Meta-YAML
Source0:        https://www.cpan.org/modules/by-module/CPAN/CPAN-Meta-YAML-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1}
%endif
%if %{with perl_CPAN_Meta_YAML_enables_extra_test}
%endif
Requires:	perl(Carp)
Requires:	perl(Fcntl)
Provides:       perl(CPAN::Meta::YAML)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Meta-YAML-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 UNINST=0
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%if %{with perl_CPAN_Meta_YAML_enables_extra_test}
make test TEST_FILES="xt/*/*.t"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.020-522
- Prepare for Oreon 11 (RP1)
