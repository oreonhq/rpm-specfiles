%global source0_hash 8444894d3ec8f6266c8c1809b68eb9ab1b4b6bd0d88647c857c5441e88493e44

Name:           perl-Geo-Functions
Version:        0.08
Release:        9%{?dist}
Summary:        Standard Geo:: functions

License:        MIT
URL:            https://metacpan.org/release/Geo-Functions
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Functions-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Geo::Constants) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-Functions-%{version}

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
%doc CONTRIBUTING.md README.md
%{perl_vendorlib}/Geo/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
