%global source0_hash 88189ae68dfbd54615ad133df07e2ec8048d06d8b9586add1227d74eb2ebb047

%global use_x11_tests 1

Name:           perl-Gtk2-Notify
Version:        0.05
Release:        59%{?dist}
Summary:        Perl interface to libnotify
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Notify
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Gtk2-Notify-%{version}.tar.gz
Patch0:         libnotify.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
# gtk2-devel needed for <gtk2perl.h> from perl-Gtk2
BuildRequires:  gtk2-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Gtk2)
# Tests:
BuildRequires:  perl(Glib) >= 1.093
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
%if %{use_x11_tests}
# X11 tests:
# Some tests invoke glib functions which try dbus-launch. Without
# dbus-launch, an warning is emmitted which causes Test::Exception to raise an
# error.
BuildRequires:  dbus-x11
# And the dbus is used to talk to org.freedesktop.Notifications server which
# can be requested by desktop-notification-daemon RPM symbol. However it can
# pull whole Gnome or KDE. So we use mimalistic `dunst' instead.
BuildRequires:  dunst
BuildRequires:  font(:lang=en)
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
%endif
Requires:       perl(Carp)

%description
Perl bindings to libnotify.  This module will allow one to use the notify
functionality from within a perl application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Notify-%{version}
%patch -P0 -p1
# Remove bundled module
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
# tests mostly bomb under mock, unfortunately
%if %{use_x11_tests}
xvfb-run -a make test
%else
make test
%endif

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gtk2*
%{_mandir}/man3/*

%changelog
%autochangelog
