%global source0_hash 00b6ddee00d854ca71f308fa038f48f7d0044250bfc676b07ee2a634afca00ed
Name:           perl-File-Find-Rule-PPI
Version:        1.07
Release:        8%{?dist}
Summary:        Add support for PPI queries to File::Find::Rule
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Rule-PPI
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Find-Rule-PPI-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Find)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::Find::Rule::PPI allows you to integrate PPI content queries into
your File::Find::Rule searches.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Find-Rule-PPI-%{version}
perl -pi -e 's/\r//' Changes

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
