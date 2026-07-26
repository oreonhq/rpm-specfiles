%global source0_hash 35696a6ba52acb32d0c3a83019dad96c0b6d1a529e407669cc4feee3b8b7be67

Name:           perl-Devel-LeakGuard-Object
Version:        0.08
Release:        29%{?dist}
Summary:        Scoped checks for object leaks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-LeakGuard-Object
Source0:        https://cpan.metacpan.org/authors/id/P/PT/PTC/Devel-LeakGuard-Object-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
# Tests only
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(latest)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
This module provides tracking of objects, for the purpose of detecting
memory leaks due to circular references or innappropriate caching schemes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-LeakGuard-Object-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
