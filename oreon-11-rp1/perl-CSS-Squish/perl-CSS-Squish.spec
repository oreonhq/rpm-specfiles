%global source0_hash 65fc0d69acd1fa33d9a4c3b09cce0fbd737d747b1fcc4e9d87ebd91050cbcb4e

Name:           perl-CSS-Squish
Version:        0.10
Release:        45%{?dist}
Summary:        Compact many CSS files into one big file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CSS-Squish
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/CSS-Squish-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# For improved tests
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)

%description
This module takes a list of CSS files and concatenates them, making sure to
honor any valid @import statements included in the files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CSS-Squish-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
