%global source0_hash af676f6090965e66a46ca37bcdfecf16f2a1d4f69c4b554dd424ab99ce50dece
Name:           perl-IP-Geolocation-MMDB
Version:        1.013
Release:        1%{?dist}
Summary:        Read MaxMind DB files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IP-Geolocation-MMDB
Source0:        https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/IP-Geolocation-MMDB-%{version}.tar.gz
Suggests:       geolite2-asn
Suggests:       geolite2-city
Suggests:       geolite2-country
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libmaxminddb)
# /oreon:deps
%description
A Perl module that reads MaxMind DB files and maps IP addresses to location
information such as country and city names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir IP-Geolocation-MMDB-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
