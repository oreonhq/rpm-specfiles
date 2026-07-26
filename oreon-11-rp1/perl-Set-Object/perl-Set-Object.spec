%global source0_hash d18c5a8a233eabbd0206cf3da5b00fcdd7b37febf12a93dcc3d1c026e6fdec45

Name: perl-Set-Object
Version: 1.42
Release: 15%{?dist}
License: Artistic-2.0
Summary: Set of objects and strings
URL: https://metacpan.org/release/Set-Object
Source0: https://cpan.metacpan.org/modules/by-module/Set/Set-Object-%{version}.tar.gz
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires: perl(AutoLoader)
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(overload)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Devel::Peek)
BuildRequires: perl(Test::More)
# Optional tests
BuildRequires: perl(Moose)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::LeakTrace)
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(threads)
BuildRequires: perl(threads::shared)
BuildRequires: perl(warnings)
Requires: perl(Scalar::Util)

%description
This modules implements a set of objects, that is, an unordered
collection of objects without duplication.

The term *objects* is applied loosely - for the sake of Set::Object,
anything that is a reference is considered an object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Set-Object-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

# clean up buildroot
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes.pod META.yml README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Set*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
