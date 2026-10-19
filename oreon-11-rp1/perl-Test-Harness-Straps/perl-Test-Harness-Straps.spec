%global source0_hash 8b00efaa35723c1a35c8c8f5fa46a99e4bc528dfa520352b54ac418ef6d1cfa8
Name:           perl-Test-Harness-Straps
Version:        0.30
Release:        48%{?dist}
Summary:        Detailed analysis of test results
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Harness-Straps
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Test-Harness-Straps-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(POSIX)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Harness is limited to printing out its results. This makes analysis
of the test results difficult for anything but a human. To make it easier
for programs to work with test results, we provide Test::Harness::Straps.
Instead of printing the results, straps provide them as raw data. You can
also configure how the tests are to be run.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Harness-Straps-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
