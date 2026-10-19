%global source0_hash 5f6efc88958afca6c4defc5727292a5aae4da40115cfebcb8d7783ee8274f38e
%global use_x11_tests 1
Name:           perl-Gtk2-GladeXML
Version:        1.008
Release:        1%{?dist}
Summary:        Create user interfaces directly from Glade XML files (deprecated)
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-GladeXML
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-GladeXML-%{version}.tar.gz
Requires:  perl(Gtk2) >= 1.000
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Glade is a free user interface builder for GTK+ and GNOME. After designing
a user interface with glade-2 the layout and configuration are saved in an XML
file. libglade is a library which knows how to build and hook up the user
interface described in the Glade XML file at application run time.

This extension module binds libglade to Perl so you can create and manipulate
user interfaces in Perl code in conjunction with Gtk2 and even Gnome2. Better
yet you can load a file's contents into a Perl scalar do a few magical regular
expressions to customize things and the load up the app. It doesn't get any
easier.

This package is deprecated. Users are advised to migrate to Gtk3::Builder Perl
module available from perl-Gtk3 package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-GladeXML-%{version}
chmod -c -x examples/*

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

    xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
