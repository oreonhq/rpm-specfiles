%global source0_hash 75a8da894eec493a21b3696b9b93e4a61c29e51fd9b2870445a7a916208e9bb9

Name:       perl-Catalyst-View-PDF-Reuse 
Version:    0.05
Release:    30%{?dist}
# lib/Catalyst/Helper/View/PDF/Reuse.pm -> GPL+ or Artistic
# lib/Catalyst/View/PDF/Reuse.pm -> GPL+ or Artistic
# lib/Template/Plugin/Catalyst/View/PDF/Reuse.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:    Create PDF files from Catalyst using Template Toolkit templates 
Source:     https://cpan.metacpan.org/authors/id/J/JO/JONALLEN/Catalyst-View-PDF-Reuse-%{version}.tar.gz 
Url:        https://metacpan.org/release/Catalyst-View-PDF-Reuse
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(Catalyst::View::TT)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::chdir)
BuildRequires: perl(parent)
BuildRequires: perl(PDF::Reuse)
BuildRequires: perl(Template::Plugin::Procedural)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)

# not picked up due to use base/parent
Requires:      perl(Catalyst::View::TT)
Requires:      perl(Template::Plugin::Procedural)

%description
Catalyst::View::PDF::Reuse provides the facility to generate PDF files
from a Catalyst application by embedding PDF::Reuse commands within a
Template::Toolkit template.  Within your template you will have access
to a 'pdf' object which has methods corresponding to all of PDF::Reuse's
functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-PDF-Reuse-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
