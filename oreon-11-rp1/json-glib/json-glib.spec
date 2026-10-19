%global source0_hash 55c5c141a564245b8f8fbe7698663c87a45a7333c2a2c56f06f811ab73b212dd
%define glib2_version 2.72.0
Name:           json-glib
Version:        1.10.8
Release:        1%{?dist}
Summary:        Library for JavaScript Object Notation format
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        https://download.gnome.org/sources/%{name}/1.10/%{name}-%{version}.tar.xz
Requires:       glib2%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  /usr/bin/rst2html5
BuildRequires:  /usr/bin/rst2man
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  python3-docutils
# /oreon:deps
%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tests
Summary: Tests for the json-glib package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The json-glib-tests package contains tests that can be used to verify
the functionality of the installed json-glib package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

%meson -Ddocumentation=enabled -Dman=true
%meson_build
%install
%meson_install
%find_lang json-glib-1.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n json-glib-devel -f %{oreon_filedir}/json-glib-devel.list
%files -n json-glib-tests -f %{oreon_filedir}/json-glib-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.8-1
- Prepare for Oreon 11 (RP1)
