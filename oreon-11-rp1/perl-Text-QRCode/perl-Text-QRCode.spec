%global source0_hash 0d5471bed596ddcd891df271c1b7983a4e39373c984d0f1ed9cb2ec4d730a173

# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/K/KU/KURIHARA
%define FullName Text-QRCode

Name: perl-%{FullName}
Summary: Perl module to generate text base QR Code
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 0.05
Release: 14%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Copy)
BuildRequires: perl(Module::Install::AutoInstall)
BuildRequires: perl(Module::Install::Can)
BuildRequires: perl(Module::Install::Compiler)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(base)
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(libqrencode)
BuildRequires: qrencode-devel >= 2.0.0

Requires: perl(XSLoader)

%description
This module allows you to generate QR Code using ' ' and '*'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{FullName}-%{version}
rm -fr inc

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/Text
%dir %{perl_vendorarch}/auto/Text/QRCode
%{perl_vendorarch}/auto/Text/QRCode/QRCode.so
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/QRCode.pm
%{_mandir}/man3/Text::QRCode.3pm.gz

%changelog
%autochangelog
