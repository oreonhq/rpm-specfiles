%global source0_hash 9a354d7ebb6125eaddc64950be17c937e20906fa79111f59bd65e0eb19dbc2c8

%global srcname Gtk2-SourceView2

Name:           perl-%{srcname}
Version:        0.12
Release:        19%{?dist}
Summary:        Perl bindings for the GtkSourceView 2.x widget
# Automatically converted from old format: GPLv2+ or Artistic 2.0 - review is highly recommended.
License:        GPL-2.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/%{srcname}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{srcname}-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(gtksourceview-2.0)
# for runtime
BuildRequires:  perl(base)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Gtk2)
# for the testsuite
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  Xvfb xauth

%{?perl_default_filter}

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

%check
xvfb-run -a -w 1 make test

%files
%doc README Changes examples
%license COPYING
%{perl_vendorarch}/*
# not needed at runtime
%exclude %{perl_vendorarch}/Gtk2/SourceView2/Install
%{_mandir}/man3/*.3*

%changelog
%autochangelog
