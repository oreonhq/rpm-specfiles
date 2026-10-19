%global source0_hash e4b77c41cfc4c8c5a035fcdc320c7bc6cfb75ef7c5a034153df1413fa1d92f13
%define glib2_version 2.58.0
%{!?with_docs: %global with_docs 1}
Name:    libsoup
Version: 2.74.3
Release:        10%{?dist}
Summary:        Soup, an HTTP library implementation
License: LGPL-2.0-only
URL: https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/%{name}/2.74/%{name}-%{version}.tar.xz
Patch:   libsoup-2.74.3-libxml2-2.12.0-includes.patch
%if %{with_docs}
%endif
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: glib-networking%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  /usr/bin/ntlm_auth
BuildRequires:  gettext
BuildRequires:  glib-networking
BuildRequires:  gtk-doc
BuildRequires:  krb5-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  vala
# /oreon:deps
%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

%package devel
Summary: Header files for the Soup library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%if %{with_docs}

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch
%description doc
This package contains developer documentation for %{name}.

# %%{with_docs}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with_docs}
%define gtkdoc_flags -Dgtk_doc=true
%else
%define gtkdoc_flags -Dgtk_doc=false
%endif
%meson %gtkdoc_flags
%meson_build
%install
%meson_install
%find_lang libsoup
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsoup-devel -f %{oreon_filedir}/libsoup-devel.list
%files -n libsoup-doc -f %{oreon_filedir}/libsoup-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.74.3-10
- Prepare for Oreon 11 (RP1)
