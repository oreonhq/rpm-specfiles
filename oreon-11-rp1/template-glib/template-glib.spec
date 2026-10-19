%global source0_hash e533ec2f6c24cc6df66ac55ac824fadd1b4a5f433a11cbf3a6b25815c0cfcfd5
Name:           template-glib
Version:        3.40.0
Release:        1%{?dist}
Summary:        A templating library for GLib
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/template-glib/
Source0:        https://download.gnome.org/sources/%{name}/3.40/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala
# /oreon:deps
%description
Template-GLib is a templating library for GLib. It includes a simple template
format along with integration into GObject-Introspection for properties and
methods. It separates the parsing of templates and the expansion of templates
for faster expansion. You can also define scope, custom functions, and more
with the embedded expression language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddocs=true
%meson_build
%install
%meson_install
%find_lang template-glib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n template-glib-devel -f %{oreon_filedir}/template-glib-devel.list

%changelog

%autochangelog
