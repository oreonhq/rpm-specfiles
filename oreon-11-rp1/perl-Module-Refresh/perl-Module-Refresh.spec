%global source0_hash e094daa909afdf6489a9e2b32733f685a2c1cb5cc8876061075486109b0def59
Name: 		perl-Module-Refresh
Version: 	0.18
Release:        1%{?dist}
Summary:        Refresh %INC files when updated on disk
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Module-Refresh
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Refresh-%{version}.tar.gz
BuildArch: 	noarch
Provides:       perl(Module::Refresh)
Provides:       perl(Module::Refresh)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module is a generalization of the functionality provided by 
Apache::StatINC. It's designed to make it easy to do simple iterative
development when working in a persistent environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Refresh-%{version}
rm -r inc

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
