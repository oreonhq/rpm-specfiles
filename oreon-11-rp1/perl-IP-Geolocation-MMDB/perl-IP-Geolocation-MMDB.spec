%global source0_hash af676f6090965e66a46ca37bcdfecf16f2a1d4f69c4b554dd424ab99ce50dece

Name:           perl-IP-Geolocation-MMDB
Version:        1.013
Release:        4%{?dist}
Summary:        Read MaxMind DB files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IP-Geolocation-MMDB
Source:         https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/IP-Geolocation-MMDB-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
# We use pkgconf instead
#BuildRequires:  perl(Alien::libmaxminddb)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libmaxminddb) >= 1.2.0
# Runtime:
BuildRequires:  perl(Math::BigInt) >= 1.999806
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Suggests:       geolite2-asn
Suggests:       geolite2-city
Suggests:       geolite2-country

%{?perl_default_filter}

%description
A Perl module that reads MaxMind DB files and maps IP addresses to location
information such as country and city names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n IP-Geolocation-MMDB-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%dir %{perl_vendorarch}/auto/IP
%dir %{perl_vendorarch}/auto/IP/Geolocation
%dir %{perl_vendorarch}/auto/IP/Geolocation/MMDB
%{perl_vendorarch}/auto/IP/Geolocation/MMDB/MMDB.so
%dir %{perl_vendorarch}/IP
%dir %{perl_vendorarch}/IP/Geolocation
%{perl_vendorarch}/IP/Geolocation/MMDB.pm
%dir %{perl_vendorarch}/IP/Geolocation/MMDB
%{perl_vendorarch}/IP/Geolocation/MMDB/Metadata.pm
%{_mandir}/man3/IP::Geolocation::MMDB.3*
%{_mandir}/man3/IP::Geolocation::MMDB::Metadata.3*

%changelog
%autochangelog
