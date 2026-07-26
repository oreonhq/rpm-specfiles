%global source0_hash a3051b214d4a314dfc36fb4963a5a45792eecb48855ff09965e9dc6e4a344776

Name:           perl-DateTime-Precise
Version:        1.05
Release:        54%{?dist}

Summary:        Perform common time and date operations with additional GPS operations

License:        LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/DateTime-Precise
Source0:        https://cpan.metacpan.org/authors/id/B/BZ/BZAJAC/DateTime-Precise-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%{?filter_setup:
%filter_from_provides /perl(bigfloat)/d
%filter_from_provides /perl(bigint)/d
%filter_from_requires /perl(DateTime::Math\/bigfloat.pl)/d
%filter_from_requires /perl(DateTime::Math\/bigint.pl)/d
%?perl_default_filter
}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(big(float|int)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(DateTime::Math::big(float|int)\\.pl\\)

%description
The purpose of this library was to replace our dependence on Unix epoch time,
which, being limited to a range of about 1970 to 2030, is inadequate for our
purposes (we have data as old as 1870). This date library effectively handles
dates from A.D. 1000 to infinity, and would probably work all the way back to 0
(ignoring, of course, the switch-over to the Gregorian calendar). The useful
features of Unix epoch time (ease of date difference calculation and date
comparison, strict ordering) are preserved, and elements such as
human-legibility are added. The library handles fractional seconds and some
date/time manipulations used for the Global Positioning Satellite system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Precise-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/DateTime::Precise.3pm.gz

%changelog
%autochangelog
