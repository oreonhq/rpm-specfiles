Name:           perl-Sort-Versions
Version:        1.62
Release:        32%{?dist}
Summary:        Perl module for sorting of revision-like numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sort-Versions
Source0:        https://cpan.metacpan.org/modules/by-module/Sort/Sort-Versions-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)

%description
A perl 5 module for sorting of revision-like numbers

Sort::Versions allows easy sorting of mixed non-numeric and numeric strings,
like the 'version numbers' that many shared library systems and revision
control packages use. This is quite useful if you are trying to deal with
shared libraries. It can also be applied to applications that intersperse
variable-width numeric fields within text. Other applications can
undoubtedly be found.

%prep
%setup -q -n Sort-Versions-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Sort
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.62-32
- Prepare for Oreon 11 (RP1)
