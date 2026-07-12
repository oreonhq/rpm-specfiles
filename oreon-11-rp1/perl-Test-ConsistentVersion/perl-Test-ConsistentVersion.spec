%global source0_hash a65abee4ac72ffd417d8622a2decb92d088301d2548fdb721be1d185c8f41bdf

Name:           perl-Test-ConsistentVersion
Version:        0.3.1
Release:        13%{?dist}
Summary:        Ensures a CPAN distribution has consistent versioning
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-ConsistentVersion
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-ConsistentVersion-v%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::Pod::Content)
BuildRequires:  perl(version)
BuildRequires:  perl(:VERSION) >= 5.6.0
# Tests:
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Needed for TEST_AUTHOR tests
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
# Dependencies:
Requires:       perl(Test::Pod::Content)

Provides:       perl(Test::ConsistentVersion)
Provides:       perl(Test::ConsistentVersion)
%description
The purpose of this module is to make it easy for other distribution
authors to have consistent version numbers within the modules (as well as
README file and Changelog) of the distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-ConsistentVersion-v%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} -c $RPM_BUILD_ROOT

%check
TEST_AUTHOR=1 ./Build test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::ConsistentVersion.3*

%changelog
%autochangelog
