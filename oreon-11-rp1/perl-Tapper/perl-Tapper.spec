%global source0_hash 1b654cb4416242f1433a69603178a9ac9bf3bac0f83f00d7e479c6801607a22d

%global pkgname Tapper

Name:           perl-Tapper
Version:        4.1.1
Release:        36%{?dist}
Summary:        A flexible and open test infrastructure
License:        BSD-2-Clause
Url:            https://metacpan.org/release/Tapper
Source0:        https://cpan.metacpan.org/authors/id/T/TA/TAPPER/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildArch:      noarch

%description
Tapper is a modular, flexible and open test infrastructure. Its only primary 
assumption is the ubiquitous use of the Test Anything Protocol (TAP). 
Internally it is based on technology known from the CPAN testing 
infrastructure, extending it with automation and advanced querying.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

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
%doc Changes Changes-3.0.md Changes-4.0.md Changes-4.1.md README Starterpage.md
%{perl_vendorlib}/Tapper*
%{_mandir}/man3/Tapper*

%changelog
%autochangelog
