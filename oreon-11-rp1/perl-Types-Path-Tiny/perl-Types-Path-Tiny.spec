%global source0_hash 593fc9faedbc69280659c0cce85168f8e7a1714cacdf8e9e6b7489be18dfe280

Name:           perl-Types-Path-Tiny
Version:        0.006
Release:        24%{?dist}
Summary:        Path::Tiny types and coercions for Moose and Moo
License:        Apache-2.0
URL:            https://metacpan.org/release/Types-Path-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Types-Path-Tiny-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Type::Library) >= 0.008
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::TypeTiny) >= 0.004
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)


Provides:       perl(Types::Path::Tiny)
%description
This module provides Path::Tiny types for Moose, Moo, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Types-Path-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
