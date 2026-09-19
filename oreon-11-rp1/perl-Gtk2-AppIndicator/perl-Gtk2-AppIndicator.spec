%global source0_hash a25cb071e214fb89b4450aa4605031eae89b7961e149b0d6e8f491c19c14a90a

# spec file for perl-Gtk2-AppIndicator
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries

Name:           perl-Gtk2-AppIndicator
Version:        0.15
Release:        44%{?dist}
Summary:        Perl extension for libappindicator
# COPYRIGHT:    GPL+ or Artistic
# LICENSE:      Artistic text
# README:       GPL+ or Artistic
## Header files exempted from copyright by LGPLv2+
# gperl.h:      LGPLv2+ (bundled from perl-Glib-devel)
# typemap:      LGPLv2+ (bundled from perl-Glib-devel)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-AppIndicator
Source0:        https://cpan.metacpan.org/modules/by-module/Gtk2/Gtk2-AppIndicator-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# ExtUtils::Constant || (File::Copy && File::Spec)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# pkgconf-pkg-config for pkg-config executed from Makefile.PL
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(appindicator-0.1)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Gtk2) >= 1.2
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Test::More)
BuildRequires:  xorg-x11-server-Xvfb
Requires:       perl(Gtk2) >= 1.2

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

%description
This Perl module gives an interface to libappindicator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-AppIndicator-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
xvfb-run -d make test

%files
%license LICENSE COPYRIGHT
%doc Changes README
%{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/Gtk2
%{_mandir}/man3/Gtk2*

%changelog
%autochangelog
