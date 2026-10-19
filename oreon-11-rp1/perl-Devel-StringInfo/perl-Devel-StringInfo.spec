%global source0_hash 290c1291341b2dea1873f6cd6bc11df01f248d3d1d70223e87a16f3fdfeea271
Name:           perl-Devel-StringInfo
Version:        0.04
Release:        1%{?dist}
Summary:        Gather information about strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR MIT
URL:            https://metacpan.org/release/Devel-StringInfo
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-StringInfo-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::HexDump::XXD)
Requires:       perl(YAML)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Data::HexDump::XXD)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(YAML)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a debugging aid that helps figure out more information
about strings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-StringInfo-%{version}

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
