%global source0_hash 7fcc1ab79eb58fb97d43e5bdd14e21791a250a204998918c62d6a171131833b1
%bcond_with perl_HTML_FormatText_WithLinks_enables_optional_test
Name:           perl-HTML-FormatText-WithLinks
Version:        0.15
Release:        32%{?dist}
Summary:        HTML to text conversion with links as footnotes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormatText-WithLinks
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STRUAN/HTML-FormatText-WithLinks-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_HTML_FormatText_WithLinks_enables_optional_test}
%endif
Requires:       perl(HTML::FormatText) >= 2
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::FormatText\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::WithBase)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::FormatText::WithLinks takes HTML and turns it into plain text but 
prints all the links in the HTML as footnotes. By default, it attempts 
to mimic the format of the lynx text based web browser's --dump option.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormatText-WithLinks-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
