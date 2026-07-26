%global source0_hash 39fc2b99a6e613da9ea977d8cb5303fa5e07e69a15248934de1217a97b964554

%global use_x11_tests 1

Name:           perl-Gtk2-TrayIcon
Version:        0.07
Release:        19%{?dist}
Summary:        Perl interface to the EggTrayIcon library (deprecated)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            https://metacpan.org/release/Gtk2-TrayIcon            
Source0:        https://cpan.metacpan.org/modules/by-module/Gtk2/Gtk2-TrayIcon-%{version}.tar.gz        
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 0.1
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib) >= 1.00
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  pkgconfig(gtk+-2.0)
# xorg-x11-proto-devel for X11/Xatom.h
BuildRequires:  xorg-x11-proto-devel
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Gtk2::TestHelper)
# Optional tests:
%if %{use_x11_tests}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(Gtk2) >= 1.00

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

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

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc examples ChangeLog README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gtk2
%{_mandir}/man3/*.3*

%changelog
%autochangelog
