%global source0_hash d1a7010d7871d8abfe72d4c1cf72e33780a6ef0ebc6acb0d2e6a44b9933f0a92
%bcond_without perl_Scalar_Properties_enables_extra_test
%global debug_package %{nil}
%undefine _package_note_file
Name:           perl-Scalar-Properties
Version:        1.100860
Release:        1%{?dist}
Summary:        Run-time properties on scalar variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-Properties
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARCEL/Scalar-Properties-%{version}.tar.gz
Patch0:         Scalar-Properties-1.100860-English-is-for-author-tests.patch
Patch3:         Scalar-Properties-1.100860-skip-MYMETA.yml.patch
BuildArch:      noarch
%if %{with perl_Scalar_Properties_enables_extra_test}
BuildConflicts: perl(Test::Perl::Critic)
BuildConflicts: perl(Pod::Wordlist::hanekomu)
%endif
Provides:       perl(Scalar::Properties)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CheckChanges)
BuildRequires:  perl(Test::DistManifest)
BuildRequires:  perl(Test::HasVersion)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Scalar::Properties attempts to make Perl more object-oriented by taking an idea
from Ruby: Everything you manipulate is an object, and the results of those
manipulations are objects themselves.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Scalar-Properties-%{version}

# Delist English from run-time dependencies, otherise t/000-report-versions.t
# may fail if build without extra tests, CPAN RT#134158
%patch -P 0 -p1

# MANIFEST.SKIP should include MYMETA.yml; otherwise, t/release-dist-manifest.t
# may fail due to it appearing unexpectedly
%patch -P 3 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%if %{with perl_Scalar_Properties_enables_extra_test}
make test AUTHOR_TESTING=1 RELEASE_TESTING=1
%else
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
