%global source0_hash 19b04616b9e1ae8dccf7cd812b702b0c31db11247958889fc794f60ed6d5f525
%bcond_with perl_HTML_Strip_enables_optional_test
Name:           perl-HTML-Strip
Version:        2.12
Release:        1%{?dist}
Summary:        Perl extension for stripping HTML markup from text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Strip
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KILINRAX/HTML-Strip-%{version}.tar.gz
%if %{with perl_HTML_Strip_enables_optional_test}
%endif
Suggests:       perl(HTML::Entities)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module simply strips HTML-like markup from text in a very quick and
brutal manner. It could quite easily be used to strip XML or SGML from text
as well; but removing HTML markup is a much more common problem, hence this
module lives in the HTML:: namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir HTML-Strip-%{version}
%oreon_prep
%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset RELEASE_TESTING
%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
