%global source0_hash 3ed85a417f534941e24def50fcc6813a19ab047cf9b497be1493ad93e522c99f

Name:           perl-Alien-libmaxminddb
Version:        2.001
Release:        3%{?dist}
Summary:        Find or download and install libmaxminddb
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-libmaxminddb
Source:         https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/Alien-libmaxminddb-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(utf8)
BuildRequires:  pkgconfig(libmaxminddb)
# Tests:
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(Test::More)
Requires:       pkgconfig(libmaxminddb)

%global debug_package %{nil}

%{?perl_default_filter}

%description
MaxMind and DP-IP.com provide geolocation databases in the MaxMind DB file
format.  This Perl module finds or installs the C library libmaxminddb,
which can read MaxMind DB files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Alien-libmaxminddb-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORLIB=%{perl_vendorarch} NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%dir %{perl_vendorarch}/Alien
%{perl_vendorarch}/Alien/libmaxminddb.pm
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien
%{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien/alien.json
%{_mandir}/man3/Alien::libmaxminddb.3*

%changelog
%autochangelog
