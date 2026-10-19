%global source0_hash a65abee4ac72ffd417d8622a2decb92d088301d2548fdb721be1d185c8f41bdf
Name:           perl-Test-ConsistentVersion
Version:        0.3.1
Release:        1%{?dist}
Summary:        Ensures a CPAN distribution has consistent versioning
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-ConsistentVersion
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-ConsistentVersion-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::Pod::Content)
Provides:       perl(Test::ConsistentVersion)
Provides:       perl(Test::ConsistentVersion)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Content)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

TEST_AUTHOR=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
