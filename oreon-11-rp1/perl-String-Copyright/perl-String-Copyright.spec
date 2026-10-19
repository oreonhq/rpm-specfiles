%global source0_hash 2e4d42405a00400891da361352498b38d9baae26d8d279c3d4e7e4626805b575
Name:           perl-String-Copyright
Version:        0.003014
Release:        9%{?dist}
Summary:        Representation of text-based copyright statements
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/String-Copyright
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/String-Copyright-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Number::Range)
BuildRequires:  perl(Set::IntSpan)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
String::Copyright Parses common styles of copyright statements and serializes
in normalized format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir String-Copyright-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
