%global source0_hash 594f5c6abc216c95cd45877c41dec56d2bc30e1d0316ad3855b0a2aa8e5d53b1

#TODO: BR: perl(Test::CheckManifest) ≥ 1.24 when available

# Run extra tests
%if ! (0%{?rhel})
%bcond_without perl_Software_License_CCpack_enables_extra_tests
%else
%bcond_with perl_Software_License_CCpack_enables_extra_tests
%endif

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

Name:		perl-Software-License-CCpack
Version:	1.11
Release:	42%{?dist}
Summary:	Software::License pack for Creative Commons' licenses
License:	LGPL-3.0-only
URL:		https://metacpan.org/release/Software-License-CCpack
Source0:	https://cpan.metacpan.org/authors/id/B/BB/BBYRD/Software-License-CCpack-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Software::License)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::CheckDeps) >= 0.010
BuildRequires:	perl(Test::More) >= 0.96
# Extra Tests
%if 0%{!?perl_bootstrap:1} && %{with perl_Software_License_CCpack_enables_extra_tests}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::DistManifest)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Mojibake)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Synopsis)
%if 0%{?fedora} < 39 && 0%{?rhel} < 10
BuildRequires:	perl(Test::Vars)
%endif
%endif
# Dependencies
# (none)

Provides:       perl(Software::License::CCpack)
%description
This "license pack" contains all of the licenses from Creative Commons, except
for CC0, which is already included in Software::License.

Note that I don't recommend using these licenses for your own CPAN modules
(most of the licenses aren't even compatible with CPAN). However, S:L modules
are useful for more than mere CPAN::Meta::license declaration, so these modules
exist for those other purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Software-License-CCpack-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1} && %{with perl_Software_License_CCpack_enables_extra_tests}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))" RELEASE_TESTING=1
%endif

%files
%license LICENSE
%doc README
%{perl_vendorlib}/Software/
%{_mandir}/man3/Software::License::CCpack.3*
%{_mandir}/man3/Software::License::CC_BY_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_4_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_4_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_ND_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_ND_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_ND_4_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_SA_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_SA_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_SA_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_NC_SA_4_0.3*
%{_mandir}/man3/Software::License::CC_BY_ND_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_ND_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_ND_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_ND_4_0.3*
%{_mandir}/man3/Software::License::CC_BY_ND_NC_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_SA_1_0.3*
%{_mandir}/man3/Software::License::CC_BY_SA_2_0.3*
%{_mandir}/man3/Software::License::CC_BY_SA_3_0.3*
%{_mandir}/man3/Software::License::CC_BY_SA_4_0.3*
%{_mandir}/man3/Software::License::CC_PDM_1_0.3*

%changelog
%autochangelog
