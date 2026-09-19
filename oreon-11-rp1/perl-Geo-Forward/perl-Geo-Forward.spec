%global source0_hash 014380d47db6e26a12f9d7f17ba5398108f1e84ca445cae240cb53fddef83e6d

Name:           perl-Geo-Forward
Version:        0.16
Release:        8%{?dist}
Summary:        Calculate geographic location from lat, lon, distance, and heading

License:        MIT
URL:            https://metacpan.org/release/Geo-Forward
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Forward-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Geo::Constants) >= 0.04
BuildRequires:  perl(Geo::Ellipsoids) >= 0.09
BuildRequires:  perl(Geo::Functions) >= 0.03
BuildRequires:  perl(Package::New)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-Forward-%{version}
perl -i -pe 's/\r//;' doc/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc CONTRIBUTING.md Changes README.md doc/
%{perl_vendorlib}/Geo/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
