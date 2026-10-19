%global source0_hash 014380d47db6e26a12f9d7f17ba5398108f1e84ca445cae240cb53fddef83e6d
Name:           perl-Geo-Forward
Version:        0.16
Release:        8%{?dist}
Summary:        Calculate geographic location from lat, lon, distance, and heading
License:        MIT
URL:            https://metacpan.org/release/Geo-Forward
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Geo-Forward-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Geo::Constants)
BuildRequires:  perl(Geo::Ellipsoids)
BuildRequires:  perl(Geo::Functions)
BuildRequires:  perl(Package::New)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
