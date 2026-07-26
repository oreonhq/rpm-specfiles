%global source0_hash fd2ca702402f22f5185b12942b5079bf95ad21cde3b97a7cf2e1919147463270

Name:           perl-failures
Version:        0.004
Release:        28%{?dist}
Summary:        Minimalist exception hierarchy generator
License:        Apache-2.0
URL:            https://metacpan.org/release/failures
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/failures-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(version)
Requires:       perl(Carp)

%description
This module lets you define an exception hierarchy quickly and simply.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n failures-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
