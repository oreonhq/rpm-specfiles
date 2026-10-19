%global source0_hash 537db7c24b315e417b0643c48e8dfcb4f958043642d1f21340335679885466e7
Name:           perl-Template-Multilingual
Version:        1.00
Release:        22%{?dist}
Summary:        Multilingual templates for Template Toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Multilingual
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOLET/Template-Multilingual-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Parser)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
