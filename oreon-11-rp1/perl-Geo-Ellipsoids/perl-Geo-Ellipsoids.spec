%global source0_hash b9e87f58e0ed58e83f8ce31d0bd87319db53c75e1343a3d0cb659a32c2ea8221

Name:           perl-Geo-Ellipsoids
Version:        0.17
Release:        3%{?dist}
Summary:        Package for standard Geo:: ellipsoid a, b, f and 1/f values

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Geo-Ellipsoids
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Ellipsoids-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Geo::Constants) >= 0.04
BuildRequires:  perl(Geo::Functions) >= 0.03
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Standard Geo:: ellipsoids a, b, f and 1/f values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-Ellipsoids-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README.md
%{perl_vendorlib}/Geo/
%{_mandir}/man3/Geo::Ellipsoids.3pm*

%changelog
%autochangelog
