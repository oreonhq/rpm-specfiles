%global source0_hash 5443899eac375c43c7273bceed27b55a881325da50096137d702b3cdf6d521ee
%global use_x11_tests 1
Name:           perl-Gtk2-Spell
Version:        1.05
Release:        1%{?dist}
Summary:        Gtk2::Spell Perl module (deprecated)
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Spell
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-Spell-%{version}.tar.gz
Requires:  perl(Gtk2) >= 1.00
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtkspell-devel
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
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Perl bindings to GtkSpell, used in concert with Gtk2::TextView. Provides
misspelled word highlighting in red and offers a right click pop-up menu with
suggested corrections.

This package is deprecated. Users are advised to use
Glib::Object::Introspection Perl module instead.

%package devel
Summary:   XS support for Gtk2::Spell (deprecated)
Requires:  %name = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:  pkgconfig(gtkspell-2.0) >= 2.0.0
%description devel
This package contains files for developing XS Perl modules which calls
Gtk2::Spell XS functions.

This package is deprecated. Users are advised to use
Glib::Object::Introspection Perl module instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Spell-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

    xvfb-run -d make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Gtk2-Spell-devel -f %{oreon_filedir}/perl-Gtk2-Spell-devel.list

%changelog

%autochangelog
