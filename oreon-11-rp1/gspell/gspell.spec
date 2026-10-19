%global source0_hash 788783b56fc3d03283b3aa29302d0b958aeca88835e10b1ec61f19e0efc7e8a4
%global glib2_version 2.44
%global gtk3_version 3.20
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           gspell
Version:        1.14.5
Release:        1%{?dist}
Summary:        Spell-checking library for GTK+
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/gspell
Source0:        https://download.gnome.org/sources/%{name}/1.14/%{name}-%{version}.tar.xz
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       iso-codes
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  vala
# /oreon:deps
%description
gspell provides a flexible API to implement the spell checking
in a GTK+ application.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Installed tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
This package contains the full API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang gspell-1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gspell-devel -f %{oreon_filedir}/gspell-devel.list
%files -n gspell-tests -f %{oreon_filedir}/gspell-tests.list
%files -n gspell-doc -f %{oreon_filedir}/gspell-doc.list

%changelog

%autochangelog
