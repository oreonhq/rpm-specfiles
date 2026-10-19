%global source0_hash 9a354d7ebb6125eaddc64950be17c937e20906fa79111f59bd65e0eb19dbc2c8
%global srcname Gtk2-SourceView2
Name:           perl-%{srcname}
Version:        0.12
Release:        1%{?dist}
Summary:        Perl bindings for the GtkSourceView 2.x widget
License:        GPL-2.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/%{srcname}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{srcname}-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  Xvfb
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  xauth
# /oreon:deps
%description
Perl bindings for the C library "libgtksourceview2" that extends the
standard GTK+ framework for multiline text editing with support for
configurable syntax highlighting, unlimited undo/redo, UTF-8 compliant
caseless searching, printing and other features typical of a source
code editor.

NOTICE: This module has been deprecated by the Gtk-Perl project.  This
means that the module will no longer be updated with security patches,
bug fixes, or when changes are made in the Perl ABI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
chmod a-x examples/*
%oreon_autofiles main

%check

xvfb-run -a -w 1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
