%global source0_hash 690667c738921de2d6516b4eb639553a571e4a8310d8031f158658536de5ab42

# Run X11 tests against a dummy X11 server
%{bcond_without perl_Gnome2_Canvas_enables_x11_test}

Name:           perl-Gnome2-Canvas
Version:        1.006
Release:        19%{?dist}
Summary:        An engine for structured graphics in Gnome2 (deprecated)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Gnome2-Canvas
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-Canvas-%{version}.tar.gz
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
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.10000
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(strict)
BuildRequires:  pkgconfig(libgnomecanvas-2.0) >= 2.0.0
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
%if %{with perl_Gnome2_Canvas_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
Requires:  perl(Gtk2) >= 1.10000

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

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

%check
%if %{with perl_Gnome2_Canvas_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README TODO
%doc canvas_demo/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gnome2*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
