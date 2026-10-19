%global source0_hash f619d2df5ea0fd91c8cf83eb54acccb5e43d9e6ec1a3f727b3d0ac15d0cf378a
%bcond_with perl_CPAN_Meta_Check_enables_extra_test
Name:		perl-CPAN-Meta-Check
Summary:        Verify requirements in a CPAN::Meta object
Version:	0.018
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Meta-Check
Source0:        https://cpan.metacpan.org/modules/by-module/CPAN/CPAN-Meta-Check-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_CPAN_Meta_Check_enables_extra_test} && !%{defined perl_bootstrap}
%endif
Provides:       perl(CPAN::Meta::Check)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module verifies if requirements described in a CPAN::Meta object are
present.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Meta-Check-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%if %{with perl_CPAN_Meta_Check_enables_extra_test} && !%{defined perl_bootstrap}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.018-7
- Prepare for Oreon 11 (RP1)
