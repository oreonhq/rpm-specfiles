%global source0_hash 8733ce4b9a9a54ec185b1d85bf4da9d9d11052882a880760ff60f9779b2d1ccb
Name: d-feet 
Version: 0.3.16
Release:        1%{?dist}
Summary:        A powerful D-Bus Debugger
License: GPL-2.0-or-later
URL: https://wiki.gnome.org/Apps/DFeet
Source0:        https://download.gnome.org/sources/d-feet/0.3/d-feet-%{version}.tar.xz
Patch0: 32.patch
BuildArch: noarch
Requires: libwnck3
Requires: python3-gobject
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-pycodestyle
# /oreon:deps
%description
D-Feet is an easy to use D-Bus debugger.

D-Bus is an RPC library used on the Desktop.  D-Feet can be used to inspect
D-Bus objects of running programs and invoke methods on those objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang d-feet --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.dfeet.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
