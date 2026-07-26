%global source0_hash 437eebed042093b365c1a90c65e53bf9ca2859dd889a0ae845fe9f9da3c6c006

Name:           perl-Algorithm-Loops
Version:        1.032
Release:        24%{?dist}
Summary:        Perl module for looping constructs
License:        Unlicense
URL:            https://metacpan.org/release/Algorithm-Loops
Source0:        https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Loops-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(warnings)

%description
Algorithm::Loops provides several functions (NestedLoops, MapCar*, Filter, 
and NextPermute*) for doing different types of looping constructs. By 
default, no functions are exported into a namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Algorithm-Loops-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.txt ex
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
