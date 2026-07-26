%global source0_hash 3a5e64e7beaafd2c64a12109e3cc0fed3db3f893b0323b43b52964fc2c0c8496

Name:           perl-DateTime-Format-RFC3339
Version:        1.10.0
Release:        3%{?dist}
Summary:        Parse and format RFC3339 datetime strings
License:        CC0-1.0
URL:            https://metacpan.org/release/DateTime-Format-RFC3339
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-RFC3339-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

%description
This module understands the RFC3339 date/time format, an ISO 8601 profile,
defined at http://tools.ietf.org/html/rfc3339.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-RFC3339-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE.txt
%doc Changes README.txt
%{perl_vendorlib}/DateTime
%{_mandir}/man3/DateTime::Format::RFC3339.3pm*

%changelog
%autochangelog
