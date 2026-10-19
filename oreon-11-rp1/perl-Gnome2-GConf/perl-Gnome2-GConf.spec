%global source0_hash e3fdd64f77d3b3e6bfc9d37109d87ad061be615da4705c167b1f7c7b030233e6
Name:           perl-Gnome2-GConf
Version:        1.047
Release:        1%{?dist}
Summary:        Perl wrappers for the GConf configuration engine (deprecated)
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gnome2-GConf
Source0:        https://cpan.metacpan.org/modules/by-module/Gnome2/Gnome2-GConf-%{version}.tar.gz
Requires:       perl(Glib) >= 1.120
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  dbus-x11
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
This module allows you to use the GConf configuration system in order to
store/retrieve the configuration of an application. The GConf system is a
powerful configuration manager based on a user daemon that handles a set of
key and value pairs, and notifies any changes of the value to every program
that monitors those keys. GConf is used by GNOME 2.x.

This package is deprecated. Users are advised to migrate to Glib::IO Perl
module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gnome2-GConf-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

xvfb-run -d make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
