Name:           perl-Class-ISA
Version:        0.36
Release:        1045%{?dist}
Summary:        Report the search path for a class's ISA tree
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-ISA
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Class-ISA-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test)
Requires:       perl(deprecate)

%description
This library provides functions that return the list (in order) of names of
(super-)classes Perl would search to find a method, with no duplicates.

%prep
%setup -q -n Class-ISA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
rm -rf %{buildroot}/%{_mandir}/man3/*
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.36-1045
- Prepare for Oreon 11 (RP1)
