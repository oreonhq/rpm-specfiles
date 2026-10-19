%global source0_hash 4b8caf527d85f7eabc63ebe9d2320e0490653c2e138b88fbf42e6f41dd3e451c
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_without bundled_rust_deps
%else
%bcond_with bundled_rust_deps
%endif
%bcond djvu %{undefined rhel}
%global __provides_exclude_from ^(%{_libdir}/papers/.*\\.so|%{_libdir}/nautilus/extensions-4/.*\\.so)$
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           papers
Version:        51.0
Release:        1%{?dist}
Summary:        View multipage documents
SourceLicense:  GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND libtiff
License:        %{shrink:
    GPL-2.0-or-later AND
    GPL-3.0-or-later AND
    LGPL-2.0-or-later AND
    LGPL-2.1-or-later AND
    MIT AND
    libtiff AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR Apache-2.0) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/GNOME/Incubator/papers
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
%if %{with djvu}
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-previewer%{?_isa} = %{version}-%{release}
Requires:       %{name}-thumbnailer%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  blueprint-compiler
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-unix-print)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  rustc
# /oreon:deps
%description
Papers is a document viewer for multiple document formats for GNOME.

%package        libs
Summary:        Libraries for the Papers document viewer
%description    libs
This package contains shared libraries needed for Papers.

%package        devel
Summary:        Support for developing backends for the Papers document viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files needed for Papers
backend development.

%package        nautilus
Summary:        Papers extension for nautilus
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       nautilus%{?_isa}
Supplements:    (nautilus and %{name})
%description    nautilus
This package contains the Papers extension for the Nautilus file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package        previewer
Summary:        Papers previewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    previewer
This package brings the Papers previewer independently from Papers.
It provides the printing preview for the GTK printing dialog.

%package        thumbnailer
Summary:        Papers thumbnailer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    thumbnailer
This package brings the Papers thumbnailer independently from Papers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi
%if %{with bundled_rust_deps}
%autosetup -p1 -n papers-%{tarball_version}
cargo vendor --versioned-dirs
%else
%autosetup -p1 -n papers-%{tarball_version}
%endif
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson \
       -Ddjvu=%{?with_djvu:enabled}%{!?with_djvu:disabled} \
       -Dintrospection=disabled \
       -Dtests=false \
       %{nil}
%meson_build
%cargo_license_summary -a
%{cargo_license -a} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%find_lang papers --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n papers-libs -f %{oreon_filedir}/papers-libs.list
%files -n papers-devel -f %{oreon_filedir}/papers-devel.list
%files -n papers-nautilus -f %{oreon_filedir}/papers-nautilus.list
%files -n papers-previewer -f %{oreon_filedir}/papers-previewer.list
%files -n papers-thumbnailer -f %{oreon_filedir}/papers-thumbnailer.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.6-1
- Import
%endif
