%global source0_hash 09fe1415e16e49a69e13c0ef6e6a4a3fd8b856f389d3f3e624d7ab3b71719f78
Name:           perl-Contextual-Return
Version:        0.004014
Release:        27%{?dist}
Summary:        Create context-sensitive return values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Contextual-Return
Source0:        https://cpan.metacpan.org/modules/by-module/Contextual/Contextual-Return-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
%global __provides_exclude ^perl\\(DB\\)$
Provides:       perl(Contextual::Return)
Provides:       perl(Contextual::Return)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Want)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows you to define return values of a perl sub that are
appropriate given the calling context.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Contextual-Return-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
