%global source0_hash 21f44e2bdabb1ee7f8e41bb996d10ac7daf35c78c498177db0c00f580a20a914
%global folks_module_version 26
Name:           folks
Epoch:          1
Version:        0.15.12
Release:        1%{?dist}
Summary:        GObject contact aggregation library
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Folks
Source0:        https://download.gnome.org/sources/folks/0.15/folks-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  python3-dbusmock
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  telepathy-glib-vala
BuildRequires:  vala
# /oreon:deps
%description
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.

%package        telepathy
Summary:        Folks telepathy backend
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    telepathy
%{name}-telepathy contains the folks telepathy backend.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    tools
%{name}-tools contains a database and import tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n folks-telepathy -f %{oreon_filedir}/folks-telepathy.list
%files -n folks-tools -f %{oreon_filedir}/folks-tools.list
%files -n folks-devel -f %{oreon_filedir}/folks-devel.list

%changelog

%autochangelog
