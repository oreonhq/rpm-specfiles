%global source0_hash e91a32b375131e980d6af3ac06512ae7c166a5b6b32980af4913b78a62f9587f

Name:           perl-Template-Plugin-HTML-Strip
Version:        0.01
Release:        28%{?dist}
Summary:        HTML::Strip filter for Template Toolkit
# lib/Template/Plugin/HTML/Strip.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Template-Plugin-HTML-Strip
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSIMMONS/Template-Plugin-HTML-Strip-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::Strip)
BuildRequires:  perl(Template::Plugin::Filter)
BuildRequires:  perl(Template::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)

%{?perl_default_filter}

%description
This module is a Template Toolkit dynamic filter, which uses HTML::Strip to
remove markup (primarily HTML, but also SGML, XML, etc) from filtered
content during template processing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Plugin-HTML-Strip-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Template*
%{_mandir}/man3/Template*

%changelog
%autochangelog
