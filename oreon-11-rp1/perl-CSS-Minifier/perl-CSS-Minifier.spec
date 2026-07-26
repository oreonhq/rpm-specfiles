%global source0_hash d0a9349b8e8b7e83ab70cf8854cfbb42ff29c1f6c7c8298f2257dd21aa0c7fef

Name:       perl-CSS-Minifier 
Version:    0.01 
Release:    48%{?dist}
# lib/CSS/Minifier.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:    Remove unnecessary whitespace from CSS files 
Source:     https://cpan.metacpan.org/authors/id/P/PM/PMICHAUX/CSS-Minifier-%{version}.tar.gz 
Url:        https://metacpan.org/release/CSS-Minifier
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
# tests
BuildRequires: perl(Test::More)

%{?perl_default_filter}

%description
This module removes unnecessary whitespace from CSS. The primary
requirement developing this module is to not break working stylesheets:
if working CSS is in input then working CSS is output. The Mac/Internet
Explorer comment hack will be minimized but not stripped and so will
continue to function.This module understands space, horizontal tab, new
line, carriage return, and form feed characters to be whitespace. Any
other characters that may be considered whitespace are not minimized.
These other characters include paragraph separator and vertical tab.For
static CSS files, it is recommended that you minify during the build
stage of web deployment. If you minify on-the-fly then it might be a
good idea to cache the minified file. Minifying static files on-the-fly
repeatedly is wasteful.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CSS-Minifier-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
