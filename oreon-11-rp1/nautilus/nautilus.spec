%global source0_hash a00db908fd65026cbd5dc634e12d189de8eba2b03f105d2425341768a5ee92fb
%bcond cloudproviders %{undefined rhel}
%global glib2_version 2.79.0
%global gnome_autoar_version 0.4.4
%global gtk4_version 4.17.5
%global libadwaita_version 1.6~beta
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           nautilus
Version:        51.0.1
Release:        1%{?dist}
Summary:        File manager for GNOME
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://apps.gnome.org/Nautilus/
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch:          default-terminal.patch
%if %{with cloudproviders}
%endif
Requires:       glib2%{_isa} >= %{glib2_version}
Requires:       gnome-autoar%{_isa} >= %{gnome_autoar_version}
Requires:       gsettings-desktop-schemas%{_isa}
Requires:       gtk4%{_isa} >= %{gtk4_version}
Requires:       gvfs%{_isa}
%if ! 0%{?flatpak}
Recommends:     gvfs-fuse%{_isa}
%endif
Requires:       libadwaita%{_isa} >= %{libadwaita_version}
Requires:       %{name}-extensions%{_isa} = %{version}-%{release}
Requires:       localsearch
Recommends:     glycin-thumbnailer%{_isa}
Recommends:     gst-thumbnailers%{_isa}
Provides:       bundled(libgd)
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  localsearch
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(gexiv2-0.16)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
Nautilus is the file manager and graphical shell for the GNOME desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the GNOME desktop.

%package extensions
Summary:        Nautilus extensions library
License:        LGPL-2.1-or-later
%description extensions
This package provides the libraries used by nautilus extensions.

%package devel
Summary:        Support for developing nautilus extensions
License:        LGPL-2.1-or-later
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       %{name}-extensions%{_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description devel
This package provides libraries and header files needed
for developing nautilus extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

# Remove -Werror from compiler flags
sed -i '/-Werror/d' meson.build

%build

%meson \
  -Ddocs=true \
  -Dextensions=true \
  -Dintrospection=true \
  -Dselinux=true \
  -Dcloudproviders=%{?with_cloudproviders:true}%{?!with_cloudproviders:false}
  %{nil}
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Nautilus.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n nautilus-extensions -f %{oreon_filedir}/nautilus-extensions.list
%files -n nautilus-devel -f %{oreon_filedir}/nautilus-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
