%global source0_hash 5443899eac375c43c7273bceed27b55a881325da50096137d702b3cdf6d521ee

%global use_x11_tests 1

Name:           perl-Gtk2-Spell
Version:        1.05
Release:        19%{?dist}
Summary:        Gtk2::Spell Perl module (deprecated)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Spell
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-Spell-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 0.1
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib) >= 1.24
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  pkgconfig(gtkspell-2.0) >= 2.0.0
%if %{use_x11_tests}
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%endif
# Tests:
BuildRequires:  perl(Test::More)
%if %{use_x11_tests}
BuildRequires:  font(:lang=en)
BuildRequires:  perl(constant)
BuildRequires:  xorg-x11-server-Xvfb
%endif
Requires:  perl(Gtk2) >= 1.00

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

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

%check
%if %{use_x11_tests}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license LICENSE
%doc README gtkspell_simple.pl AUTHORS ChangeLog NEWS
%{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/Gtk2
%exclude %{perl_vendorarch}/Gtk2/Spell/Install
%{_mandir}/man3/*.3*

%files devel
%{perl_vendorarch}/Gtk2/Spell/Install

%changelog
%autochangelog
