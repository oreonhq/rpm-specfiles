%global source0_hash 98523c8192f2e8184042e5a2e172bd767ac289dd2e480f35f680dce32160905b

Name:           perl-Template-GD
Version:        2.66
Release:        52%{?dist}
Summary:        GD plugin(s) for the Template Toolkit
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-GD
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABW/Template-GD-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GD::Graph3d), perl(GD::Graph), perl(GD::Text)
BuildRequires:  perl(Template), perl(Test::More)
Requires:  perl(Template), perl(GD::Text), perl(GD::Graph), perl(GD::Graph3d)

%description
The Template-GD distribution provides a number of Template Toolkit
plugin modules to interface with Lincoln Stein's GD modules.  These in
turn provide an interface to Thomas Boutell's GD graphics library.

These plugins were distributed as part of the Template Toolkit until
version 2.15 released in February 2006.  At this time they were
extracted into this separate distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-GD-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/Template/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
