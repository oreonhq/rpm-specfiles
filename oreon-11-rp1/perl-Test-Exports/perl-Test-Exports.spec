%global source0_hash 01c1ef9a4c159024c10813bf9c43c896fc98d65de79824f875260bd844216857

Name:           perl-Test-Exports
Version:        1
Release:        11%{?dist}
Summary:        Test that modules export the right symbols
# 2-clause BSD with advertising
# c.f. lib/Test/Exports.pm
License:        BSD-2-Clause

URL:            http://metacpan.org/dist/Test-Exports/
Source0:        http://cpan.metacpan.org/authors/id/B/BM/BMORROW/Test-Exports-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

BuildRequires:  perl(B)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More) >= 0.65
BuildRequires:  perl(Test::Most) >= 0.23
BuildRequires:  perl(Test::Tester) >= 0.08

BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

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

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
