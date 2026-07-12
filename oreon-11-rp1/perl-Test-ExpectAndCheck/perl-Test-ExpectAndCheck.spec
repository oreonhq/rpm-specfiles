%global source0_hash e638a601f8af144340decc40433d97d8679eb326d4595e0c7821235045e601ed

Name:           perl-Test-ExpectAndCheck
Version:        0.08
Release:        2%{?dist}
Summary:        Expect/check-style unit testing with object methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Test-ExpectAndCheck
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-ExpectAndCheck-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Future::Deferred)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
# test requirements
BuildRequires:  perl(Future)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Builder::Tester) >= 1.302000

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(Test::ExpectAndCheck::_

Provides:       perl(Test::ExpectAndCheck)
%description
This package creates objects that assist in writing unit tests with mocked
object instances. Each mock instance will expect to receive a given list of
method calls. Each method call is checked that it received the right
arguments, and will return a prescribed result. At the end of each test,
each object is checked to ensure all the expected methods were called.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-ExpectAndCheck-%{version}

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
