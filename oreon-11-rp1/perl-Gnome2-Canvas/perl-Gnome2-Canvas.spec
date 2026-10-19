%global source0_hash 690667c738921de2d6516b4eb639553a571e4a8310d8031f158658536de5ab42
%{bcond_without perl_Gnome2_Canvas_enables_x11_test}
Name:           perl-Gnome2-Canvas
Version:        1.006
Release:        1%{?dist}
Summary:        An engine for structured graphics in Gnome2 (deprecated)
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Gnome2-Canvas
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-Canvas-%{version}.tar.gz
%if %{with perl_Gnome2_Canvas_enables_x11_test}
%endif
Requires:  perl(Gtk2) >= 1.10000
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
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
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
The Gnome Canvas is an engine for structured graphics that offers a rich
imaging model, high-performance rendering, and a powerful, high level API.

It offers a choice of two rendering back-ends, one based on GDK for extremely
fast display, and another based on Libart, a sophisticated, antialiased,
alpha-compositing engine. This widget can be used for flexible display of
graphics and for creating interactive user interface elements.

This package is deprecated. Users are advised to migrate to perl-Cairo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gnome2-Canvas-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

%if %{with perl_Gnome2_Canvas_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
