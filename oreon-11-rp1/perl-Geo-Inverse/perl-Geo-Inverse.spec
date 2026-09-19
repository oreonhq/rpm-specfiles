%global source0_hash 59b0ffab3ab44d24c5c6f42e653b089df02434337dbdc47517f9830cf199d9a4

Name:           perl-Geo-Inverse
Version:        0.09
Release:        3%{?dist}
Summary:        Calculate geographic distance from a lat & lon pair

License:        MIT
URL:            https://metacpan.org/release/Geo-Inverse
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Inverse-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
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
BuildRequires:  perl(constant)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Number::Delta)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-Inverse-%{version}

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
%doc CONTRIBUTING.md Changes README.md
%{perl_vendorlib}/Geo/
%{_mandir}/man3/Geo*.3pm*

%changelog
%autochangelog
