%global source0_hash 43d6dae64dd716b50980e8de4d815784ea9736af906cf72435894d63e21b4fe6
Name:           perl-Test-NoPlan
Version:        0.0.6
Release:        40%{?dist}
Summary:        Check perl test files for no_plan
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NoPlan
Source0:        https://cpan.metacpan.org/authors/id/D/DU/DUNCS/Test-NoPlan-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
It is a good idea to ensure you have defined how many tests should be run
within each test script - to catch cases where tests bomb out part way through
so you know how many tests were not actually run. This module checks all your
test plan files to ensure 'no_plan' is not used.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-NoPlan-v%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
