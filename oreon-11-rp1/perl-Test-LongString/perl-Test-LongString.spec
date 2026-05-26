Name:		perl-Test-LongString
Version:	0.17
Release:	33%{?dist}
Summary:	Perl module to test long strings
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-LongString
Source0:	https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Test-LongString-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 abc4349eaf04d1bec1e464166a3018591ea846d8f3c5c9c8af4ac4905d3e974f
%global source0_file Test-LongString-0.17.tar.gz
# oreon url source checksums end

BuildArch:	noarch

BuildRequires:	%{__make}
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# Required by the tests
BuildRequires:	perl(Test::Builder) >= 0.12
BuildRequires:	perl(Test::Builder::Tester) >= 1.04

BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Pod) >= 1.14 


%description
This module provides some drop-in replacements for the string comparison
functions of Test::More, but which are more suitable when you test against
long strings. If you've ever had to search for text in a multi-line string
like an HTML document, or find specific items in binary data, this is the
module for you.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-LongString-0.17.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "abc4349eaf04d1bec1e464166a3018591ea846d8f3c5c9c8af4ac4905d3e974f" || { echo "oreon: Source0 SHA256 mismatch for Test-LongString-0.17.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-LongString-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-33
- Prepare for Oreon 11 (RP1)
