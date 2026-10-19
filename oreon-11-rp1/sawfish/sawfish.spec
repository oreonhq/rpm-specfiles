%global source0_hash d7585be0ee45a4dcebf72952ffc2aa7035e683fe091a792e409fcebedbc96d85
Name:           sawfish
Version:        1.13.0
Release:        1%{?dist}
Summary:        An extensible window manager for the X Window System
License:        GPL-2.0-or-later AND Artistic-2.0
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/%{name}/%{name}_%{version}.tar.bz2
Patch0:         bool.patch
Requires:       control-center-filesystem
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       librep >= 0.92.3
Requires:       rep-gtk >= 0.90.7
%define rep_execdir %(pkg-config librep --variable=repcommonexecdir)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  gtk2-devel
BuildRequires:  kde-filesystem
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXft-devel
BuildRequires:  libXtst-devel
BuildRequires:  librep-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  rep-gtk-devel
BuildRequires:  texinfo
# /oreon:deps
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
%global oreon_srcdir %{name}_%{version}
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sawfish-devel -f %{oreon_filedir}/sawfish-devel.list

%changelog

%autochangelog
