%global source0_hash 1e3014ce1455817ec2ef74d09efdfb6835d8a372ed9a16efb5919ef7b821957a
%global branch 1.28
Name:        caja
Summary:        File manager for MATE
Version:     %{branch}.0
Release:        1%{?dist}
License:     GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:         http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:      caja_0001-caja-file-operations-fix-caption-button-in-destinati.patch
Patch2:      caja_0003-wayland-background-use-mate-appearance-properties-if.patch
Patch3:      caja_0004-build-remove-configure-dependency-on-perl-1789.patch
Patch4:      caja_0005-wayland-ensure-windows-can-be-moved-if-compositor-is.patch
Patch5:      caja_0009-caja-file-operations-fix-estimate-for-queued-copy-17.patch
Patch6:      caja_0010-caja-file-operations-restart-timer-also-for-moves.patch
Requires:   filesystem
Requires:   redhat-menus
Requires:   gvfs
Requires:       %{name}-core-extensions%{?_isa} = %{version}-%{release}
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cairo-gobject-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  exempi-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  libSM-devel
BuildRequires:  libexif-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
# /oreon:deps
%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop,
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote file systems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the MATE desktop.

%package core-extensions
Summary:  Mate-file-manager extensions library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description core-extensions
This package provides the libraries used by caja extensions.

# needed for using mate-text-editor (pluma) as stanalone in another DE
%package schemas
Summary:  Mate-file-manager schemas
License:  LicenseRef-Callaway-LGPLv2+
%description schemas
This package provides the gsettings schemas for caja.

%package devel
Summary:  Support for developing mate-file-manager extensions
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# disable startup notification
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-computer.desktop.in.in
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-home.desktop.in.in

#Patch2
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
        --disable-static \
        --disable-schemas-compile \
        --disable-update-mimedb \
        --enable-wayland
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/.icon-theme.cache
mkdir -p $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0
desktop-file-install                              \
    --delete-original                             \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/prelink.conf.d
cat << EOF > ${RPM_BUILD_ROOT}%{_sysconfdir}/prelink.conf.d/caja.conf
-b %{_libdir}/caja/
-b %{_libdir}/libcaja-extension.so.*
-b %{_libexecdir}/caja-convert-metadata
-b %{_bindir}/caja
-b %{_bindir}/caja-autorun-software
-b %{_bindir}/caja-connect-server
-b %{_bindir}/caja-file-management-properties
EOF
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles caja-core-extensions usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles caja-schemas usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles caja-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n caja-core-extensions -f %{oreon_filedir}/caja-core-extensions.list
%files -n caja-schemas -f %{oreon_filedir}/caja-schemas.list
%files -n caja-devel -f %{oreon_filedir}/caja-devel.list

%changelog

%autochangelog
