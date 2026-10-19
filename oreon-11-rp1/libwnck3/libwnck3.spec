%global source0_hash 6af8ac41a8f067ade1d3caaed254a83423b5f61ad3f7a460fcacbac2e192bdf7
%global source_name libwnck
Summary:        Window Navigator Construction Kit
Name: libwnck3
Version: 43.3
Release:        1%{?dist}
URL: http://download.gnome.org/sources/%{source_name}/
Source0:        http://download.gnome.org/sources/%{source_name}/43/%{source_name}-%{version}.tar.xz
License: LGPL-2.0-or-later
Requires:      startup-notification
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libXres-devel
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
# /oreon:deps
%description
libwnck (pronounced "libwink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libwnck
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{source_name}-%{version} -p1

%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%find_lang %{source_name}-3.0 --with-gnome --all-name
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libwnck3-devel -f %{oreon_filedir}/libwnck3-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 43.3-1
- Prepare for Oreon 11 (RP1)
