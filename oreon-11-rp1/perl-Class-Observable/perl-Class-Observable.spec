%global source0_hash 6df32e9fe5f008891fc4efa4e4f45eaa1404d30220459c8fc8a501f0a7cf2e69

Name:           perl-Class-Observable
Version:        2.004
Release:        8%{?dist}
Summary:        Allow other classes and objects to respond to events in yours
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Observable
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Observable-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Config)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
Requires:       perl(warnings)

%description
If you have ever used Java, you may have run across the
java.util.Observable class and the java.util.Observer interface. With them
you can decouple an object from the one or more objects that wish to be
notified whenever particular events occur.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Observable-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
