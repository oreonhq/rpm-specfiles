%global source0_hash c419e308cdc82af1c25d6b8d07b2ff26347a622b7a63ec20856abe8db4051f82
Name:       perl-CSS-Minifier-XS
Version:    0.13
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        XS based CSS minifier
Source0:        https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
Url:        https://metacpan.org/release/CSS-Minifier-XS
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CSS::Minifier)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Test::DiagINC)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(blib)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
