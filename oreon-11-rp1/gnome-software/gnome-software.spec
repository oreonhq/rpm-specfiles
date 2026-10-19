%global source0_hash 834b6035e61e36dd72339eb3e15d299b472ae0b393467a5bb36bb0045e0ba123
%global appstream_version 0.16.4
%global flatpak_version 1.14.1
%global fwupd_version 1.6.2
%global glib2_version 2.76.0
%global gtk4_version 4.17.5
%global json_glib_version 1.6.0
%global libadwaita_version 1.8.0
%global libxmlb_version 0.3.4
%global packagekit_version 1.2.5
%global dnf5_version 5.4.2
%bcond webapps %[!0%{?rhel}]
%bcond malcontent %[!0%{?rhel}]
%bcond rpmostree %[!0%{?rhel}]
%bcond dkms %[!0%{?rhel}]
%bcond packagekit 0
%bcond dnf5 0
%define gs_plugin_version 23
%global tarball_version %(echo %{version} | tr '~' '.')
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins-%{gs_plugin_version}/.*\\.so.*$
Name:      gnome-software
Version:   51.0
Release:        1%{?dist}
Summary:        A software center for GNOME
License:   GPL-2.0-or-later
URL:       https://apps.gnome.org/Software
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
%if %{with dnf5}
Patch:        0002-plain-package-update-notification.patch
%endif
%if 0%{?fedora} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
ExcludeArch:    %{ix86}
%endif
%if %{with malcontent}
%endif
%if %{with packagekit}
%endif
%if %{with rpmostree}
%endif
Requires: appstream-data
Requires: appstream%{?_isa} >= %{appstream_version}
%if %{with webapps}
Requires: epiphany-runtime%{?_isa}
%endif
%if %{with dnf5}
Requires: dnf5daemon-server%{?_isa} >= %{dnf5_version}
Requires: dnf5daemon-server-polkit
Requires: libdnf5-plugin-appstream%{?_isa}
Requires: rpm-plugin-dbus-announce%{?_isa}
%endif
Requires: flatpak%{?_isa} >= %{flatpak_version}
Requires: flatpak-libs%{?_isa} >= %{flatpak_version}
Requires: fwupd%{?_isa} >= %{fwupd_version}
Requires: glib2%{?_isa} >= %{glib2_version}
%if !0%{?rhel} || (0%{?oreon} >= 11)
Requires: gnome-app-list
%endif
Requires: gnome-menus%{?_isa}
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gtk4 >= %{gtk4_version}
Requires: json-glib%{?_isa} >= %{json_glib_version}
Requires: iso-codes
Requires: libadwaita >= %{libadwaita_version}
Requires: librsvg2%{?_isa}
Requires: libxmlb%{?_isa} >= %{libxmlb_version}
%if %{with packagekit}
Recommends: PackageKit%{?_isa} >= %{packagekit_version}
%endif
Recommends: %{name}-fedora-langpacks
Obsoletes: gnome-software-snap < 3.33.1
Obsoletes: gnome-software-editor < 3.35.1
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdnf)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(ostree-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(rpm-ostree-1)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  systemd
# /oreon:deps
%description
gnome-software is an application that makes it easy to add, remove
and update software in the GNOME desktop.

%package devel
Summary: Headers for building external gnome-software plugins
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
These development files are for building gnome-software plugins outside
the source tree. Most users do not need this subpackage installed.

%package fedora-langpacks
Summary: Contains fedora-langpacks plugin
Requires: %{name}%{?_isa} = %{version}-%{release}
%description fedora-langpacks
The fedora-langpacks plugin ensures langpacks packages are installed
for the current locale.

%if %{with rpmostree}
%package rpm-ostree
Summary: rpm-ostree backend for gnome-software
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: rpm-ostree%{?_isa}
Supplements: (gnome-software%{?_isa} and rpm-ostree%{?_isa})
%description rpm-ostree
gnome-software is an application that makes it easy to add, remove
and update software in the GNOME desktop.

This package includes the rpm-ostree backend.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S gendiff -n %{name}-%{tarball_version}

%build

%meson \
    -Dsnap=false \
%if %{with malcontent}
    -Dmalcontent=true \
%else
    -Dmalcontent=false \
%endif
    -Dgudev=true \
%if %{with packagekit}
    -Dpackagekit=true \
    -Dpackagekit_autoremove=true \
%else
    -Dpackagekit=false \
%endif
%if %{with dnf5}
    -Ddnf5=true \
%endif
    -Dexternal_appstream=false \
%if %{with rpmostree}
    -Drpm_ostree=true \
%else
    -Drpm_ostree=false \
%endif
%if %{with webapps}
    -Dwebapps=true \
    -Dhardcoded_foss_webapps=true \
    -Dhardcoded_proprietary_webapps=false \
%else
    -Dwebapps=false \
    -Dhardcoded_foss_webapps=false \
    -Dhardcoded_proprietary_webapps=false \
%endif
%if %{with dkms}
    -Ddkms=true \
%else
    -Ddkms=false \
%endif
    -Dtests=false
%meson_build
%install
%meson_install
rm %{buildroot}%{_libdir}/gnome-software/plugins-%{gs_plugin_version}/libgs_plugin_dpkg.so
rm %{buildroot}%{_libdir}/gnome-software/plugins-%{gs_plugin_version}/libgs_plugin_dummy.so
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.Software.desktop \
    --set-key=X-AppInstall-Package --set-value=%{name}
cat >> %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.software-fedora.gschema.override << FOE
[org.gnome.software]
%if 0%{?rhel} || (0%{?oreon} >= 11)
official-repos = [ 'rhel-%{?rhel}' ]
%else
official-repos = [ 'anaconda', 'fedora', 'fedora-debuginfo', 'fedora-source', 'koji-override-0', 'koji-override-1', 'rawhide', 'rawhide-debuginfo', 'rawhide-source', 'updates', 'updates-debuginfo', 'updates-source', 'updates-testing', 'updates-testing-debuginfo', 'updates-testing-source', 'fedora-modular', 'fedora-modular-debuginfo', 'fedora-modular-source', 'rawhide-modular', 'rawhide-modular-debuginfo', 'rawhide-modular-source', 'fedora-cisco-openh264', 'fedora-cisco-openh264-debuginfo' ]
required-repos = [ 'fedora', 'updates' ]
packaging-format-preference = [ 'flatpak:fedora-testing', 'flatpak:fedora', 'rpm' ]
%endif
FOE
%find_lang %name --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnome-software-devel -f %{oreon_filedir}/gnome-software-devel.list
%files -n gnome-software-fedora-langpacks -f %{oreon_filedir}/gnome-software-fedora-langpacks.list
%files -n gnome-software-rpm-ostree -f %{oreon_filedir}/gnome-software-rpm-ostree.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.2-1
- Import
