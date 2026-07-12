%global source0_hash a418935483def0a46259a50bff6320842792a5a02777192667de222475253075

Name:           perl-Test-Most
Version:        0.42
Release:        1%{?dist}
Summary:        Perl module with test functions and features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Most
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Most-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dumper::Names) >= 0.03
BuildRequires:  perl(Exception::Class) >= 1.14
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep) >= 0.119
BuildRequires:  perl(Test::Differences) >= 0.64
BuildRequires:  perl(Test::Exception) >= 0.43
BuildRequires:  perl(Test::Harness) >= 3.35
BuildRequires:  perl(Test::More) >= 1.302047
BuildRequires:  perl(Test::Warn) >= 0.30
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
# Not automatically detected
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Dumper::Names) >= 0.03
Requires:       perl(Test::Deep) >= 0.119
Requires:       perl(Test::Differences) >= 0.64
Requires:       perl(Test::Exception) >= 0.43
Requires:       perl(Test::Harness) >= 3.35
Requires:       perl(Test::More) >= 1.302047
Requires:       perl(Test::Warn) >= 0.30
Requires:       perl(Time::HiRes)

Provides:       perl(Test::Most)
%description
Most commonly needed test functions and features. This module provides you with 
the most commonly used testing functions and gives you a bit more fine-grained 
control over your test suite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Most-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Most.3*
%{_mandir}/man3/Test::Most::Exception.3*

%changelog
%autochangelog
