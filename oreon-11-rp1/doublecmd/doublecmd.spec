%global source0_hash edefc76bace7c3446579f9a57fe6243f9ec9cdb09cd1f19bd4cb0abf8c4b5191

%global debug_package %{nil}

Name:           doublecmd
Version:        1.2.4
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels

# Full licenses description in licensecheck.txt file
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND MPL-1.1 AND MPL-2.0 AND Apache-2.0 AND BSD-2-Clause AND Zlib
URL:            http://doublecmd.sourceforge.net
Source0:        https://sourceforge.net/projects/%{name}/files/Double%20Commander%20Source/%{name}-%{version}-src.tar.gz
Source1:        %{name}-qt.desktop
Source2:        licensecheck.txt
Source3:        io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
Source4:        io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
Source5:        %{name}-qt6.desktop

BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(pango)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

ExclusiveArch:  x86_64 aarch64

%description
Double Commander GTK2 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    gtk
Double Commander GTK is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt
Summary:        Twin-panel (commander-style) file manager (Qt5)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    qt
Double Commander QT6 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt6
Summary:        Twin-panel (commander-style) file manager (Qt6)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    qt6
Double Commander QT6 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        common
Summary:        Common files for Double Commander

Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}

%description    common
Common files for Double Commander GTK2 and Qt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0
# Sure to not use libbz2 and libssh2 bundling
rm -rf libraries

%build
lcl=qt5 ./build.sh beta
mv ./%name ./%name-qt
mv ./%name.zdli ./%name-qt.zdli
./clean.sh

lcl=qt6 ./build.sh beta
mv ./%name ./%name-qt6
mv ./%name.zdli ./%name-qt6.zdli
./clean.sh

lcl=gtk2 ./build.sh beta

%install
install/linux/install.sh --install-prefix=%{buildroot}
install -pm 0755 ./%{name}-qt %{buildroot}%{_libdir}/%{name}/%{name}-qt
ln -s ../%{_lib}/%{name}/%{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -pm 0644 ./%{name}-qt.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt.zdli
install -pm 0755 ./%{name}-qt6 %{buildroot}%{_libdir}/%{name}/%{name}-qt6
ln -s ../%{_lib}/%{name}/%{name}-qt6 %{buildroot}%{_bindir}/%{name}-qt6
install -pm 0644 ./%{name}-qt6.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt6.zdli
desktop-file-install %{SOURCE1}
desktop-file-install %{SOURCE5}
cp %{SOURCE2} .
install -D -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt6.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml

%files gtk
%{_libdir}/%{name}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}.zdli
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml

%files qt
%{_libdir}/%{name}/%{name}-qt
%{_bindir}/%{name}-qt
%{_libdir}/%{name}/%{name}-qt.zdli
%{_datadir}/applications/%{name}-qt.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml

%files qt6
%{_libdir}/%{name}/%{name}-qt6
%{_bindir}/%{name}-qt6
%{_libdir}/%{name}/%{name}-qt6.zdli
%{_datadir}/applications/%{name}-qt6.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml

%files common
%doc doc/changelog.txt doc/README.txt licensecheck.txt
%license doc/COPYING.LGPL.txt doc/COPYING.modifiedLGPL.txt doc/COPYING.txt
%exclude %{_libdir}/%{name}/%{name}
%exclude %{_libdir}/%{name}/%{name}-qt
%exclude %{_libdir}/%{name}/%{name}-qt6
%exclude %{_libdir}/%{name}/%{name}.zdli
%exclude %{_libdir}/%{name}/%{name}-qt.zdli
%exclude %{_libdir}/%{name}/%{name}-qt6.zdli
%exclude %{_bindir}/%{name}
%exclude %{_bindir}/%{name}-qt
%exclude %{_bindir}/%{name}-qt6
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/doublecmd.svg
%{_datadir}/polkit-1/actions/org.doublecmd.root.policy

%changelog
%autochangelog
