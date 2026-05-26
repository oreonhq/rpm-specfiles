# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f619d2df5ea0fd91c8cf83eb54acccb5e43d9e6ec1a3f727b3d0ac15d0cf378a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_CPAN_Meta_Check_enables_extra_test
%else
%bcond_with perl_CPAN_Meta_Check_enables_extra_test
%endif

Name:		perl-CPAN-Meta-Check
Summary:	Verify requirements in a CPAN::Meta object
Version:	0.018
Release:	7%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Meta-Check
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.018.tar.gz

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(base)
BuildRequires:	perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Metadata) >= 1.000023
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test
BuildRequires:	perl(blib)
BuildRequires:	perl(CPAN::Meta) >= 2.120920
BuildRequires:	perl(Env)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.88
%if %{with perl_CPAN_Meta_Check_enables_extra_test} && !%{defined perl_bootstrap}
# Break a build cycle: perl-Pod-Coverage-TrustPod → perl-Pod-Eventual
# → perl-Mixin-Linewise → perl-Sub-Exporter → perl-Params-Util
# → perl-Config-AutoConf → perl-File-Slurper → perl-Test-Warnings
# → perl-CPAN-Meta-Check
# Extra tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
%endif
# Dependencies
# (none)

%description
This module verifies if requirements described in a CPAN::Meta object are
present.

%prep
%oreon_verify_sources
%setup -q -n CPAN-Meta-Check-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_CPAN_Meta_Check_enables_extra_test} && !%{defined perl_bootstrap}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::Check.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.018-7
- Prepare for Oreon 11 (RP1)
