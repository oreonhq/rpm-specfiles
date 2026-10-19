%global source0_hash 2facfb530ddcd20c03ed4758ef934e832626c393e2cacd23fc1249b7ed0e4246
%global debug_package %{nil}
Name: gtk-doc
Version: 1.37.0
%global source_series %(echo %{version} | cut -d. -f1-2)
Release:        1%{?dist}
Summary:        API documentation generation tool for GTK+ and GNOME
License: GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL: https://gitlab.gnome.org/GNOME/gtk-doc/
Source0:        https://download.gnome.org/sources/%{name}/%{source_series}/%{name}-%{version}.tar.xz
Requires: docbook-utils /usr/bin/xsltproc docbook-style-xsl
Requires: python3-pygments
Requires: python3-lxml
Requires: cmake-filesystem
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  dblatex
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-pygments
BuildRequires:  yelp-tools
# /oreon:deps
%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build

%meson
%meson_build
%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gtk-doc/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
