%global source0_hash 969f59b64531614eba3ebba2c4c32e7ad817a9deac17e1984520cedcc4705eac

Name:           perl-Module-Starter-Plugin-CGIApp
Version:        0.44
Release:        31%{?dist}
Summary:        Template based module starter for CGI apps
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Module-Starter-Plugin-CGIApp
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JALDHAR/Module-Starter-Plugin-CGIApp-%{version}.tar.gz
# https://github.com/jaldhar/Module-Starter-Plugin-CGIApp/pull/3
Patch0:         Module-Starter-Plugin-CGIApp-0.44-starter.patch
BuildArch:      noarch
buildrequires:  findutils
buildrequires:  perl-generators
buildrequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::DirCompare)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Module::Starter) >= 1.71
BuildRequires:  perl(Module::Starter::App)
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::CGIApp)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Titanium)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Module::Starter) >= 1.71

%{?perl_default_filter}
# Remove under-specified dependencies:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Starter\\)$

%description
This is a plugin for Module::Starter that builds you a skeleton
CGI::Application module with all the extra files needed to package it for
CPAN. You can customize the output using HTML::Template.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Starter-Plugin-CGIApp-%{version}
%patch -P0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install --destdir $RPM_BUILD_ROOT  create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?!_with_signature_test:rm t/00-signature.t}
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/cgiapp-starter
%{_bindir}/titanium-starter
%{_mandir}/man1/cgiapp-starter.1.gz
%{_mandir}/man1/titanium-starter.1.gz
%{_mandir}/man3/*

%changelog
%autochangelog
