%global source0_hash 32a1ebcd803fa10eefca553bc3cedd43596a759dc3975adebd22688823c36aea
Name:		perl-Test-MinimumVersion
Version:	0.101083
Release:        9%{?dist}
Summary:        Check whether your code requires a newer perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-MinimumVersion
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Test::MinimumVersion) = %{version}
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Check whether your code requires a newer perl than you think.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-MinimumVersion-%{version}
find -type f -exec chmod -x {} \;

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

%autochangelog
