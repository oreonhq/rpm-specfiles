%global source0_hash bcdc102e22f63f55e63166d5c708e91c113570e6a30a874345a88609e83a9912
Name:           mate-media
Version:        1.28.1
Release:        1%{?dist}
Summary:        MATE media programs
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-panel-devel
# /oreon:deps
%description
This package contains a few media utilities for the MATE desktop,
including a volume control.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-panelapplet=yes \
        --enable-statusicon=yes \
        --enable-wayland \
        --enable-in-process
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-volume-control.desktop
rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart/mate-volume-control-status-icon.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
