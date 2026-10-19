%global source0_hash 6cfbcb6a45064446ec8aa0ee1a7dddc420b54469303344187aef84d2c7f3e2c6
Name:       perl-Module-Util
Version:    1.09
Release:        38%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Module name tools and transformations
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-%{version}.tar.gz
Url:        https://metacpan.org/release/Module-Util
BuildArch:  noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralize some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Util-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
