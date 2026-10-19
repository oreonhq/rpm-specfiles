%global source0_hash 2506c88d4eb21b274b1085f806c918dcc97fff69e16d1249e6e19d943625e468
Name:           perl-Test-Metrics-Any
Version:        0.01
Release:        1%{?dist}
Summary:        Assert that code produces metrics via Metrics::Any
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Metrics-Any/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Metrics-Any-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::Metrics::Any::_predicate\\)$
Provides:       perl(Test::Metrics::Any)
Provides:       perl(Test::Metrics::Any)
# oreon:deps
BuildRequires:  perl(Metrics::Any)
BuildRequires:  perl(Metrics::Any::Adapter)
BuildRequires:  perl(Metrics::Any::Adapter::Test)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
