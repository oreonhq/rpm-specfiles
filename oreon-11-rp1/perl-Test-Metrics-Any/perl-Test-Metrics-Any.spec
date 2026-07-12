%global source0_hash 2506c88d4eb21b274b1085f806c918dcc97fff69e16d1249e6e19d943625e468

Name:           perl-Test-Metrics-Any
Version:        0.01
Release:        19%{?dist}
Summary:        Assert that code produces metrics via Metrics::Any
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Metrics-Any/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Metrics-Any-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Metrics::Any::Adapter)
BuildRequires:  perl(Metrics::Any::Adapter::Test)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Metrics::Any)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.88

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::Metrics::Any::_predicate\\)$

Provides:       perl(Test::Metrics::Any)
Provides:       perl(Test::Metrics::Any)
%description
This test module helps write unit tests which assert that the code under
test reports metrics via Metrics::Any.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Metrics-Any-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
