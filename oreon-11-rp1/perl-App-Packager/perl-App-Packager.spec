%global source0_hash 5681416be6fd7897be98483c4ea28eb0dde0cc65b3c20e68d47b3044decf287a

# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName App-Packager

Name: perl-%{FullName}
Summary: Abstract interface to a number of common packagers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 1.440
Release: 8%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
App::Packager provides an abstract interface to a number of common
packagers, trying to catch as much common behavior as possible.

The main purpose is to have uniform access to application specific
resources.

Supported packagers are PAR::Packer, Cava::Packager and unpackaged. In the
latter case, the packager functions are emulated via Cava::Packager which
provides fallback for unpackaged use.

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
