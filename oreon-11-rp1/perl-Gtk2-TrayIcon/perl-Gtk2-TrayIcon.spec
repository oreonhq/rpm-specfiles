%global source0_hash 39fc2b99a6e613da9ea977d8cb5303fa5e07e69a15248934de1217a97b964554
%global use_x11_tests 1
Name:           perl-Gtk2-TrayIcon
Version:        0.07
Release:        19%{?dist}
Summary:        Perl interface to the EggTrayIcon library (deprecated)
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            https://metacpan.org/release/Gtk2-TrayIcon            
Source0:        https://cpan.metacpan.org/modules/by-module/Gtk2/Gtk2-TrayIcon-%{version}.tar.gz
Requires:       perl(Gtk2) >= 1.00
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
This module allows a Perl developer to embed an arbitrary widget in a System
Tray like the Gnome notification area.

This package is deprecated. The users are advised to migrate to
Gtk3::StatusIcon from perl-Gtk3 package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-TrayIcon-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

    xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
