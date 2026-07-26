%global source0_hash 64268e15983a9df47e1d9199a491f394e89f542e54afb33f4b78f3f318e09ab9

Name: 		perl-Text-Wrapper
Version: 	1.05
Release: 	36%{?dist}
Summary:	Simple word wrapping perl module
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Text-Wrapper
Source0: 	https://cpan.metacpan.org/modules/by-module/Text/Text-Wrapper-%{version}.tar.gz

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Carp)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildArch: 	noarch

%description
This module provides simple word wrapping.  It breaks long lines, but does
not alter spacing or remove existing line breaks.  If you're looking for
more sophisticated text formatting, try the Text::Format module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Wrapper-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test RELEASE_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
%autochangelog
