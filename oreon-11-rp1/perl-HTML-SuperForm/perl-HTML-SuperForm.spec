%global source0_hash 11c4b74be704a2ef1a87040d9e50dba740b7302e34671e21e878b1d1faf6f95e

Name:           perl-HTML-SuperForm
Version:        1.09
Release:        46%{?dist}
Summary:        HTML form generator
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-SuperForm
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JALLWINE/HTML-SuperForm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module provides an interface for generating basic HTML form elements much
like HTML::StickyForms does. The main difference is HTML::SuperForm returns
HTML::SuperForm::Field objects rather than plain HTML. This allows for more
flexibility when generating forms for a complex application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-SuperForm

# Upstream left an old version of the module in the latest tarball
rm lib/HTML/SuperForm.pm.orig

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
