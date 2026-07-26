%global source0_hash e3fdd64f77d3b3e6bfc9d37109d87ad061be615da4705c167b1f7c7b030233e6

Name:           perl-Gnome2-GConf
Version:        1.047
Release:        19%{?dist}
Summary:        Perl wrappers for the GConf configuration engine (deprecated)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gnome2-GConf
Source0:        https://cpan.metacpan.org/modules/by-module/Gnome2/Gnome2-GConf-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.2000
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(File::Spec)
BuildRequires:  pkgconfig(gconf-2.0) >= 2.0.0
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(overload)
# Tests:
# The tests need D-Bus with X11
BuildRequires:  dbus-x11
BuildRequires:  font(:lang=en)
BuildRequires:  perl(constant)
BuildRequires:  perl(Test::More)
BuildRequires:  xorg-x11-server-Xvfb
Requires:       perl(Glib) >= 1.120

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$

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

%check
xvfb-run -d make test

%files
%license copyright.pod
%doc AUTHOR ChangeLog NEWS README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gnome2*
%{_mandir}/man3/*

%changelog
%autochangelog
