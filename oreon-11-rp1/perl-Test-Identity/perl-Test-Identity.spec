%global source0_hash 2f0205009aed152668182aafa16357ab1f47b4cbc001e89871b67387ef8e5f23

Name:           perl-Test-Identity
Version:        0.01
Release:        38%{?dist}
Summary:        Assert the referential identity of a reference
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Identity
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module provides a single testing function, identical. It asserts that
a given reference is as expected; that is, it either refers to the same
object or is undef. It is similar to Test::More::is except that it uses
refaddr, ensuring that it behaves correctly even if the references under
test are objects that overload stringification or numification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Identity-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
