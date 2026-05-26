Name: 		perl-Number-Compare
Version: 	0.03
Release: 	42%{?dist}
Summary: 	Perl module for numeric comparisons
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Number-Compare
Source0: 	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 83293737e803b43112830443fb5208ec5208a2e6ea512ed54ef8e4dd2b880827
%global source0_file Number-Compare-0.03.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Number-Compare-0.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "83293737e803b43112830443fb5208ec5208a2e6ea512ed54ef8e4dd2b880827" || { echo "oreon: Source0 SHA256 mismatch for Number-Compare-0.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
