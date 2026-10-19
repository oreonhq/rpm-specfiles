%global source0_hash a418935483def0a46259a50bff6320842792a5a02777192667de222475253075
Name:           perl-Test-Most
Version:        0.42
Release:        2%{?dist}
Summary:        Perl module with test functions and features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Most
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Test-Most-%{version}.tar.gz
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dumper::Names)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
