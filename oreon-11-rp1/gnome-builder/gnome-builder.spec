%global source0_hash 4524a57ff9dd640fbb05d972eac8d4b5b2a8c2ca29062f2bc5dec8d5c6058cee
%global __provides_exclude_from ^%{_libdir}/gnome-builder
%global privlibs .*-private|libide|libgnome-builder-plugins
%global __requires_exclude ^(%{privlibs}).*\\.so.*
%global tarball_version %%(echo %{version} | tr '~' '.')
%global glib2_version 2.75.0
%global gtk4_version 4.15.5
%global json_glib_version 1.2.0
%global jsonrpc_glib_version 3.43.0
%global libadwaita_version 1.6~alpha
%global libdex_version 0.2
%global libpeas_version 1.99.0
%global libspelling_version 0.3.0
%global libgit2_glib_version 1.1.0
%global template_glib_version 3.36.1
Name:           gnome-builder
Version:        50~rc.1
Release:        1%{?dist}
Summary:        IDE for writing GNOME-based software
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-50.rc.1.tar.xz
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       jsonrpc-glib%{?_isa} >= %{jsonrpc_glib_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libdex%{?_isa} >= %{libdex_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}
Requires:       libpeas%{?_isa} >= %{libpeas_version}
Requires:       libpeas-loader-gjs%{?_isa} >= %{libpeas_version}
Requires:       libspelling%{?_isa} >= %{libspelling_version}
Requires:       template-glib%{?_isa} >= %{template_glib_version}
Requires:       flatpak-builder
Recommends:     clang
Recommends:     clang-tools-extra
Recommends:     ctags
Recommends:     meson
Recommends:     sysprof-agent
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  clang-devel
BuildRequires:  ctags
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
%description
Builder attempts to be an IDE for writing software for GNOME. It does not try
to be a generic IDE, but one specialized for writing GNOME software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dhelp=true
%meson_build
%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gnome-builder/plugins/
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Builder.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Builder.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnome-builder-devel -f %{oreon_filedir}/gnome-builder-devel.list

%changelog

%autochangelog
