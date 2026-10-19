%global source0_hash 1b022a0a6451827d060ee9cbfe9b2d8edbac2a3d7155cbee33ea93274b830fb5
%oreon_bootstrap
%bcond_with perl_CPAN_Changes_enables_extra_test
Name:		perl-CPAN-Changes
Summary:        Read and write Changes files
Version:	0.500005
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Changes
Source0:        https://cpan.metacpan.org/modules/by-module/CPAN/CPAN-Changes-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_CPAN_Changes_enables_extra_test}
%endif
Provides:       perl(CPAN::Changes)
Provides:       perl(Test::CPAN::Changes)
Provides:       perl(CPAN::Changes)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Changes-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%if %{with perl_CPAN_Changes_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.500005-3
- Prepare for Oreon 11 (RP1)
