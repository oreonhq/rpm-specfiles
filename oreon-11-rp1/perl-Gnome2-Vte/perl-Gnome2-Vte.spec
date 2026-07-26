%global source0_hash 1634431bf0763b56db6afeea008dcd5fc9ed2f5c5ca27715ead616f588f4d98c

# Execute X11 test
%bcond_without perl_Gnome2_Vte_enables_x11_test

Name:           perl-Gnome2-Vte
Version:        0.12
Release:        19%{?dist}
Summary:        Perl interface to the Gtk2 Virtual Terminal Emulation library (deprecated)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gnome2-Vte
Source0:        https://cpan.metacpan.org/modules/by-module/Gnome2/Gnome2-Vte-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(strict)
BuildRequires:  pkgconfig(vte) >= 0.10
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Glib) >= 1.01
BuildRequires:  perl(Test::More)
%if %{with perl_Gnome2_Vte_enables_x11_test}
# coreutils for /bin/ls
BuildRequires:  coreutils
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif

%{?perl_default_filter}

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

%check
%if %{with perl_Gnome2_Vte_enables_x11_test}
    xvfb-run -a make test
%else
    make test
%endif

%files
%license LICENSE
%doc ChangeLog.pre-git maps NEWS README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gnome2*
%{_mandir}/man3/*

%changelog
%autochangelog
