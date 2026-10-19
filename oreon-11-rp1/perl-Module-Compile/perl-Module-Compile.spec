%global source0_hash 8090cfbb61123437eefec3e3bed86005d1f7c5a529fb6fda2ebebc6564b9aa10
Name:           perl-Module-Compile
Version:        0.38
Release:        18%{?dist}
Summary:        Perl Module Compilation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Compile
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Compile-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Digest::SHA1) >= 2.13
Requires:       perl(Filter::Util::Call)
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Digest::SHA1\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module provides a system for writing modules that compile other
Perl modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Compile-%{version}
rm -rf inc/ && sed -i -e '/^inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
