%global source0_hash 3ed85a417f534941e24def50fcc6813a19ab047cf9b497be1493ad93e522c99f
Name:           perl-Alien-libmaxminddb
Version:        2.001
Release:        3%{?dist}
Summary:        Find or download and install libmaxminddb
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-libmaxminddb
Source0:        https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/Alien-libmaxminddb-%{version}.tar.gz
Requires:       pkgconfig(libmaxminddb)
%global debug_package %{nil}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libmaxminddb)
# /oreon:deps
%description
MaxMind and DP-IP.com provide geolocation databases in the MaxMind DB file
format.  This Perl module finds or installs the C library libmaxminddb,
which can read MaxMind DB files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Alien-libmaxminddb-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORLIB=%{perl_vendorarch} NO_PACKLIST=1 NO_PERLLOCAL=1
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
