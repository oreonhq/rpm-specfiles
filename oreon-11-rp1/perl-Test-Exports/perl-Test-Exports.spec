%global source0_hash 01c1ef9a4c159024c10813bf9c43c896fc98d65de79824f875260bd844216857
Name:           perl-Test-Exports
Version:        1
Release:        1%{?dist}
Summary:        Test that modules export the right symbols
License:        BSD-2-Clause
URL:            http://metacpan.org/dist/Test-Exports/
Source0:        http://cpan.metacpan.org/authors/id/B/BM/BMORROW/Test-Exports-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(B)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides simple test functions for testing other modules'
import methods. Testing is currently limited to checking which subs have
been imported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Exports-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
