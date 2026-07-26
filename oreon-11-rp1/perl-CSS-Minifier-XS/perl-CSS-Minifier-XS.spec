%global source0_hash c419e308cdc82af1c25d6b8d07b2ff26347a622b7a63ec20856abe8db4051f82

Name:       perl-CSS-Minifier-XS
Version:    0.13
Release:    18%{?dist}
# lib/CSS/Minifier/XS.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    XS based CSS minifier
Source:     https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
Url:        https://metacpan.org/release/CSS-Minifier-XS

BuildRequires: findutils
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(CSS::Minifier)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(blib)
BuildRequires: perl(Test::DiagINC)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
'CSS::Minifier::XS' is a CSS "minifier". It's designed to remove
unnecessary white-space and comments from CSS files, while also
*not* breaking the CSS. 'CSS::Minifier::XS' is similar in function
to 'CSS::Minifier', but is substantially faster as it's written
in XS and not just pure Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CSS-Minifier-XS-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
