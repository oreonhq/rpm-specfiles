%global source0_hash b4a44fddfc055cc42ee67bfd8939354793da7512ea04f30578d42dc6a701112a
Name:      perl-Astro-SunTime
Summary:        Calculates sun rise/set times
Version:   0.06
Release:        25%{?dist}
License:   GPL-3.0-only
URL:       https://metacpan.org/release/Astro-SunTime
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildArch: noarch
Requires:  perl(Time::ParseDate)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::ParseDate)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Astro::SunTime Perl module provides a function interface to calculate sun
rise/set times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Astro-SunTime-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_build pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
