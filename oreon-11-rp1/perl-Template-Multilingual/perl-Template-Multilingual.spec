%global source0_hash 537db7c24b315e417b0643c48e8dfcb4f958043642d1f21340335679885466e7

Name:           perl-Template-Multilingual
Version:        1.00
Release:        22%{?dist}
Summary:        Multilingual templates for Template Toolkit
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Template-Multilingual
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOLET/Template-Multilingual-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime deps
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Parser)
BuildRequires:  perl(base)
# test deps
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This subclass of Template Toolkit's Template class supports multilingual
templates: templates that contain text in several languages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Multilingual-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Template*
%{_mandir}/man3/Template*

%changelog
%autochangelog
