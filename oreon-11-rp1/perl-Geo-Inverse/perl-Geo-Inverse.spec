%global source0_hash 59b0ffab3ab44d24c5c6f42e653b089df02434337dbdc47517f9830cf199d9a4
Name:           perl-Geo-Inverse
Version:        0.09
Release:        1%{?dist}
Summary:        Calculate geographic distance from a lat & lon pair
License:        MIT
URL:            https://metacpan.org/release/Geo-Inverse
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Inverse-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Geo::Constants)
BuildRequires:  perl(Geo::Ellipsoids)
BuildRequires:  perl(Geo::Functions)
BuildRequires:  perl(Package::New)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
