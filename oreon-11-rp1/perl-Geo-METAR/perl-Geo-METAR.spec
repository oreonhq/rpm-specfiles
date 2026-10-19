%global source0_hash c73ab84b9af41295d5d226660fba3bfd6da3472060cd63457bcffce50893e536
%global pkgname Geo-METAR
Name:           perl-Geo-METAR
Version:        1.15
Release:        1%{?dist}
Summary:        Perl module for accessing aviation weather information
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Geo-METAR
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOOS/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Geo::METAR is Perl module for accessing aviation weather information. 
Referring to things like a cloud altitudes, temperature, wind, dew point,
and so on.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor 
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
