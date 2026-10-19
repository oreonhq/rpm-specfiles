%global source0_hash 88189ae68dfbd54615ad133df07e2ec8048d06d8b9586add1227d74eb2ebb047
%global use_x11_tests 1
Name:           perl-Gtk2-Notify
Version:        0.05
Release:        1%{?dist}
Summary:        Perl interface to libnotify
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Notify
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Gtk2-Notify-%{version}.tar.gz
Patch0:         libnotify.patch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  dbus-x11
BuildRequires:  dunst
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
# /oreon:deps
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
%oreon_autofiles main

%check

xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
