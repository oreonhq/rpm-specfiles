%global source0_hash ad23059165bf1fcabe389ebcbaea8339077764b6217cf090f532f66ee42fa62d
%global pkgname Net-Random
Name:           perl-Net-Random
Version:        2.33
Release:        1%{?dist}
Summary:        A module gets random data from online sources
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Random
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
Suggests:       perl(LWP::Protocol::https)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module can get random data from online sources such as websites.

This module is unsupported, unmaintained, obsolete, and DEPRECATED.
It is recommended to switch to using Crypt::URandom.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

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
