%global source0_hash 19b04616b9e1ae8dccf7cd812b702b0c31db11247958889fc794f60ed6d5f525

# Perform optional tests
%bcond_with perl_HTML_Strip_enables_optional_test

Name:           perl-HTML-Strip
Version:        2.12
Release:        12%{?dist}
Summary:        Perl extension for stripping HTML markup from text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-Strip
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KILINRAX/HTML-Strip-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(HTML::Entities)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
# Test::Kwalitee not used
BuildRequires:  perl(Test::More)
%if %{with perl_HTML_Strip_enables_optional_test}
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
Suggests:       perl(HTML::Entities)

%{?perl_default_filter}

%description
This module simply strips HTML-like markup from text in a very quick and
brutal manner. It could quite easily be used to strip XML or SGML from text
as well; but removing HTML markup is a much more common problem, hence this
module lives in the HTML:: namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n HTML-Strip-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset RELEASE_TESTING
%{make_build} test

%files
%doc Changes README
%{perl_vendorarch}/auto/HTML*
%{perl_vendorarch}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
