%global source0_hash 2bd556289a6d44ad2ee74803258bb0b0050d246f1e81caab0b263c303acf0c82
Name: 		perl-File-Find-Rule
Version: 	0.35
Release:        1%{?dist}
Summary:        Perl module implementing an alternative interface to File::Find
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/File-Find-Rule
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Find-Rule-%{version}.tar.gz
BuildArch: 	noarch
Provides:       perl(File::Find::Rule)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::Find::Rule is a friendlier interface to File::Find.  It allows
you to build rules which specify the desired files and directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-Find-Rule-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35-3
- Prepare for Oreon 11 (RP1)
