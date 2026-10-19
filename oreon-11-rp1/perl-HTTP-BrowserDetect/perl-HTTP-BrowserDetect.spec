%global source0_hash d4dbfddd9df6e9c35d151c9b00544211b38cb8c3aee4350a540bddaa75203669
Name:           perl-HTTP-BrowserDetect
Summary:        Determine the Web browser, version, and platform from an HTTP user agent string
Version:        3.45
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-BrowserDetect
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-BrowserDetect-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available
at http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-BrowserDetect-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
