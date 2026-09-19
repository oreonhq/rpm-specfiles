%global source0_hash 012cca57baf8335b163c734b789d5966dde47f0bd8a579433f4852ca666fffe2

# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName String-Interpolate-Named

Name: perl-%{FullName}
Summary: Interpolated named arguments in string
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 1.06
Release: %autorelease
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1

BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
String::Interpolate::Named provides a single function, interpolate,
that takes a string and substitutes named variables by target texts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
