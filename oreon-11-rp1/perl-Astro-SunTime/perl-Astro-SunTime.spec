%global source0_hash b4a44fddfc055cc42ee67bfd8939354793da7512ea04f30578d42dc6a701112a

Name:      perl-Astro-SunTime
Summary:   Calculates sun rise/set times 
Version:   0.06
Release:   25%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:   GPL-3.0-only
URL:       https://metacpan.org/release/Astro-SunTime
Source:    https://cpan.metacpan.org/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildArch: noarch

BuildRequires: make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Test)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)

Requires:  perl(Time::ParseDate)

%description
Astro::SunTime Perl module provides a function interface to calculate sun
rise/set times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Astro-SunTime-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -delete

%check
%make_build test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/Astro
%{perl_vendorlib}/Astro/SunTime.pm

%changelog
%autochangelog
