%global source0_hash d7585be0ee45a4dcebf72952ffc2aa7035e683fe091a792e409fcebedbc96d85

Name:           sawfish
Version:        1.13.0
Release:        13%{?dist}
Summary:        An extensible window manager for the X Window System
License:        GPL-2.0-or-later AND Artistic-2.0
# GPLv2+ is for Sawfish
# Artistic 2.0 is for sounds
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/%{name}/%{name}_%{version}.tar.bz2
Patch0:         bool.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXft-devel
BuildRequires:  libXtst-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  gettext
BuildRequires:  kde-filesystem
BuildRequires:  desktop-file-utils
BuildRequires:  librep-devel >= 0.92.3
BuildRequires:  rep-gtk-devel >= 0.90.7
BuildRequires:  gdk-pixbuf2-xlib-devel
Requires:       control-center-filesystem
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       librep >= 0.92.3
Requires:       rep-gtk >= 0.90.7

%define rep_execdir %(pkg-config librep --variable=repcommonexecdir)

%description
Sawfish is an extensible window manager which uses a Lisp-based
scripting language.  All window decorations are configurable and the
basic idea is to have as much user-interface policy as possible
controlled through the Lisp language.  Configuration can be
accomplished by writing Lisp code in a personal .sawfishrc file, or
using a GTK+ interface.  Sawfish is mostly GNOME compliant

%package devel
Summary:        Development files for Sawfish
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Include files for Sawfish development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}_%{version}

%build
./autogen.sh --nocfg
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
gzip -9nf %{buildroot}%{_infodir}/sawfish*
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot}%{_libdir} -name \*.a -exec rm '{}' \;
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;
# Fix main.jl (sawfish-config) for rpmlint
sed -i -e '/^\#!/,/^!\#/d' %{buildroot}%{_datadir}/sawfish/lisp/sawfish/cfg/main.jl

rm %{buildroot}%{_datadir}/xsessions/sawfish-kde4.desktop
rm -rf %{buildroot}%{_datadir}/ksmserver
rm -rf %{buildroot}%{_datadir}/kde4

desktop-file-validate %{buildroot}%{_datadir}/applications/sawfish.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/sawfish-config.desktop
desktop-file-validate %{buildroot}%{_datadir}/gnome/wm-properties/sawfish-wm.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-kde5.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-lumina.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-mate.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-xfce.desktop

%files -f %{name}.lang
%license COPYING COPYING.SOUNDS
%doc README README.IMPORTANT doc/*
%{_bindir}/*
%{rep_execdir}/sawfish
%{_libdir}/sawfish
%{_datadir}/sawfish
%{_datadir}/applications/sawfish.desktop
%{_datadir}/applications/sawfish-config.desktop
%{_datadir}/gnome/wm-properties/sawfish-wm.desktop
%{_datadir}/xsessions/sawfish.desktop
%{_datadir}/xsessions/sawfish-kde5.desktop
%{_datadir}/xsessions/sawfish-lumina.desktop
%{_datadir}/xsessions/sawfish-mate.desktop
%{_datadir}/xsessions/sawfish-xfce.desktop
%{_datadir}/icons/hicolor/32x32/apps/sawfish-config.png
%{_mandir}/man1/sawfish*.gz
%{_infodir}/sawfish*

%files devel
%{_includedir}/sawfish
%{_libdir}/pkgconfig/sawfish.pc

# Note about rpmlint warning:
# W: devel-file-in-non-devel-package /usr/bin/sawfish-config
# This is sawfish GUI configurator, not devel config script.

%changelog
%autochangelog
