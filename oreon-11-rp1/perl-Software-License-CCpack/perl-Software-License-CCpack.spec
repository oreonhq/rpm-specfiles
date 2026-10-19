%global source0_hash 594f5c6abc216c95cd45877c41dec56d2bc30e1d0316ad3855b0a2aa8e5d53b1
%bcond_with perl_Software_License_CCpack_enables_extra_tests
%global debug_package %{nil}
%undefine _package_note_file
Name:		perl-Software-License-CCpack
Version:	1.11
Release:        42%{?dist}
Summary:        Software::License pack for Creative Commons' licenses
License:	LGPL-3.0-only
URL:		https://metacpan.org/release/Software-License-CCpack
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBYRD/Software-License-CCpack-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1} && %{with perl_Software_License_CCpack_enables_extra_tests}
%if 0%{?fedora} < 39 && 0%{?rhel} < 10 && 0%{?oreon} < 11
%endif
%endif
Provides:       perl(Software::License::CCpack)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%if 0%{!?perl_bootstrap:1} && %{with perl_Software_License_CCpack_enables_extra_tests}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))" RELEASE_TESTING=1
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
