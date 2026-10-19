%global source0_hash 258807feb2e7bac523707d6b3daf2d9439e7135123cbe795183d5aaa6fd691ed
Name:           nemo
Summary:        File manager for Cinnamon
Version:        6.6.4
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        nemo-fedora.gschema.override
Patch0:         remove_desktop_search.patch
Patch1:         Don-t-scale-text-size-when-zooming.patch
Patch2:         fix_mount_action.patch
ExcludeArch:   %{ix86}
Requires:       redhat-menus
Requires:       gvfs-archive%{?_isa}
Requires:       gvfs-fuse%{?_isa}
Requires:       gvfs-goa%{?_isa}
Requires:       xapps%{?_isa} >= 2.2.0
Recommends:     xapp-symbolic-icons
Recommends:     cinnamon-translations >= 6.6.0
Recommends:     nemo-search-helpers
Recommends:     folder-color-switcher-nemo
Requires:       %{name}-extensions%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  python3-gobject-base
BuildRequires:  python3-packaging
# /oreon:deps
%description
Nemo is the file manager and graphical shell for the Cinnamon desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the Cinnamon desktop.

%package extensions
Summary: Nemo extensions library
License: LicenseRef-Callaway-LGPLv2+
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description extensions
This package provides the libraries used by nemo extensions.

%package search-helpers
Summary: Nemo search helpers
License: LicenseRef-Callaway-LGPLv2+
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   exif
Requires:   ghostscript
Requires:   odt2txt
Requires:   poppler-utils
Requires:   python3-xlrd
%description search-helpers
This package provides the search helpers used by nemo.

%package devel
Summary: Support for developing nemo extensions
License: LicenseRef-Callaway-LGPLv2+
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-extensions%{?_isa} = %{version}-%{release}
%description devel
This package provides libraries and header files needed
for developing nemo extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -D deprecated_warnings=false \
  -D gtk_doc=false \
  -D selinux=true
%meson_build
%install
%meson_install
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/glib-2.0/schemas/nemo-fedora.gschema.override
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  --add-only-show-in "X-Cinnamon;Budgie" \
  %{buildroot}%{_datadir}/applications/nemo-autostart.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/{nemo,nemo-autorun-software}.desktop
mkdir -p %{buildroot}%{_libdir}/nemo/extensions-3.0/
rm %{buildroot}%{_datadir}/nemo/search-helpers/id3.nemo_search_helper
rm %{buildroot}%{_datadir}/nemo/search-helpers/pdf2txt.nemo_search_helper
%ldconfig_scriptlets extensions
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nemo-extensions -f %{oreon_filedir}/nemo-extensions.list
%files -n nemo-search-helpers -f %{oreon_filedir}/nemo-search-helpers.list
%files -n nemo-devel -f %{oreon_filedir}/nemo-devel.list

%changelog

%autochangelog
