%global source0_hash 1634431bf0763b56db6afeea008dcd5fc9ed2f5c5ca27715ead616f588f4d98c
%bcond_without perl_Gnome2_Vte_enables_x11_test
Name:           perl-Gnome2-Vte
Version:        0.12
Release:        19%{?dist}
Summary:        Perl interface to the Gtk2 Virtual Terminal Emulation library (deprecated)
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gnome2-Vte
Source0:        https://cpan.metacpan.org/modules/by-module/Gnome2/Gnome2-Vte-%{version}.tar.gz
%if %{with perl_Gnome2_Vte_enables_x11_test}
%endif
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
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
BuildRequires:  pkgconfig(vte)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Gnome2::Vte exposes the GNOME Virtual Terminal Emulator API to Perl
applications.

This package is deprecated. The users are advised to migrate to Glib::IO Perl
module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gnome2-Vte-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%if %{with perl_Gnome2_Vte_enables_x11_test}
    xvfb-run -a make test
%else
    make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
