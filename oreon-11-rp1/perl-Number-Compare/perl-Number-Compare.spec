Name: 		perl-Number-Compare
Version: 	0.03
Release: 	42%{?dist}
Summary: 	Perl module for numeric comparisons
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Number-Compare
Source0: 	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires:	%{__make}
BuildRequires:	perl-generators
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)

%description
Number::Compare compiles a simple comparison to an anonymous subroutine,
which you can call with a value to be tested again.

%prep
%setup -q -n Number-Compare-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/Number
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-42
- Prepare for Oreon 11 (RP1)
