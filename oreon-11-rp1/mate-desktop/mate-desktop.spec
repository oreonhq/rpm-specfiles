%global source0_hash 32bb4b792014b391c1e1b8ae9c18a82b4d447650984b4cba7d28e95564964aa2
%global branch 1.28
Summary:        Shared code for mate-panel, mate-session, caja, etc
Name:          mate-desktop
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Version:       %{branch}.2
Release:        1%{?dist}
URL:           http://mate-desktop.org
Source0:        http://pub.%{name}.org/releases/%{branch}/%{name}-%{version}.tar.xz
Source1:       mate-fedora-f34.gschema.override
Source2:       mate-rhel.gschema.override
Source3:       mate-mimeapps.list
Source4:       80-mate-compiz.preset
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-configs = %{version}-%{release}
Requires: redhat-menus
Requires: xdg-user-dirs-gtk
Requires: mate-control-center-filesystem
Requires: mate-panel
Requires: mate-notification-daemon
Requires: mate-user-guide
Suggests:  imsettings-mate
# oreon:deps
BuildRequires:  cairo-gobject-devel
BuildRequires:  dconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  iso-codes-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  startup-notification-devel
# /oreon:deps
%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package libs
Summary:   Shared libraries for libmate-desktop
License:   LicenseRef-Callaway-LGPLv2+
%description libs
Shared libraries for libmate-desktop

%package configs
Summary:    Configurations for Mate desktop
License:    LicenseRef-Callaway-LGPLv2+
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%description configs
Configurations for Mate desktop

%package devel
Summary:    Libraries and headers for libmate-desktop
License:    LicenseRef-Callaway-LGPLv2+
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                                                 \
     --enable-gtk-doc                                      \
     --disable-schemas-compile                             \
     --with-x                                              \
     --disable-static                                      \
     --with-pnp-ids-path="%{_datadir}/hwdata/pnp.ids"      \
     --enable-gtk-doc-html                                 \
     --enable-introspection=yes
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-about.desktop
desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-color-select.desktop
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %SOURCE3 %{buildroot}/%{_datadir}/applications/mate-mimeapps.list
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-desktop-libs -f %{oreon_filedir}/mate-desktop-libs.list
%files -n mate-desktop-configs -f %{oreon_filedir}/mate-desktop-configs.list
%files -n mate-desktop-devel -f %{oreon_filedir}/mate-desktop-devel.list

%changelog

%autochangelog
