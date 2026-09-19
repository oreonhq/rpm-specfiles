%global source0_hash 141df0b73d30c944aef0d3bb96fb4b124e71439cdbfd220280158a8a87a328e5

Name:           perl-Package-Pkg
Version:        0.0020
Release:        39%{?dist}
Summary:        Handy package munging utilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Package-Pkg
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Package-Pkg-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Try::Tiny)
# Tests
BuildRequires:  perl(Test::Most)

%{?perl_default_filter}

%description
Package::Pkg is a collection of useful, miscellaneous package-munging
utilities. Functionality is accessed via the imported pkg keyword, although
you can also invoke functions directly from the package (Package::Pkg).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Package-Pkg-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
