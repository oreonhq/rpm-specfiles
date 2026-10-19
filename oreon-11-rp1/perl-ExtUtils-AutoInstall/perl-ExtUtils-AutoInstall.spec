%global source0_hash 0fe48f78b5ee39acb3be38a7a039789abc46195af411297dabec294c2851027f
Name: 		perl-ExtUtils-AutoInstall
Version: 	0.64
Release:        1%{?dist}
Summary:        Automatic install of dependencies via CPAN
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/ExtUtils-AutoInstall
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/ExtUtils-AutoInstall-%{version}.tar.gz
Patch0:		eai.patch
BuildArch: 	noarch
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(CPAN)
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
# /oreon:deps
%description
ExtUtils::AutoInstall lets module writers specify a more sophisticated
form of dependency information than the PREREQ_PM option offered by 
ExtUtils::MakeMaker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-AutoInstall-%{version}
%patch -P0 -p1
rm -r inc/

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --defaultdeps NO_PACKLIST=1 NO_PERLLOCAL=1
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
